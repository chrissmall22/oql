import sys
import argparse
import ConfigParser
import requests
import json


class EventHandler(object):

    def __init__(self, config, logger):

        self.__cloud = config.get('DEFAULT', 'cloud')
        self.__url =  config.get(self.__cloud, 'eventhub_url')
        self.__apiKey = config.get(self.__cloud, 'X-ApiKey')
        self.__cloudRegion = config.get(self.__cloud, 'X-CloudRegion')
        self.__logger = logger


    def __printMessage(self, message):

        __instance_Id = message['payload']['instance_id']
        print('\n' + 'instance_id: ' + __instance_Id)

        __tanant_id = message['payload']['tenant_id'] 
        print('tenant_id: ' + __tanant_id + '\n')
        
        self.__logger.info(json.dumps(message, indent = 4))
        print ('')


    def __provisionServer(self, eventMessage):

        if (eventMessage != None):
            try:
                instance_Id = eventMessage['payload']['instance_id']
                correltion_Id = self.__cloudRegion + ":" + instance_Id
                request_headers = {'Content-Type': 'application/json', 'X-ApiKey': self.__apiKey, 'X-CorrelationId': correltion_Id, 'X-CloudRegion': self.__cloudRegion}           
                response = requests.post(self.__url, data=json.dumps(eventMessage), headers=request_headers, verify=False)  # TODO - set verify=True after get valid cert

            except requests.exceptions.RequestException as ex:
                self.__logger.exception(ex)
                return False

            self.__logger.info("")
            result = json.loads(response.text)
            self.__logger.info(json.dumps(result, indent = 4))

            if response.status_code == 200:
                return True

            elif response.status_code == 404 or response.status_code == 400:  # Check to see if Bad Request and Not Found
                self.__logger.error("\n provisionServer() returned an error %s, the response is:\n%s" % (response.status_code, response.text))
                return True

            else:
                self.__logger.error("\n provisionServer() returned an error %s, the response is:\n%s" % (response.status_code, response.text))
                return None


    def __deprovisionServer(self, eventMessage):

        if (eventMessage != None):
            try:
                instance_Id = eventMessage['payload']['instance_id']
                correltion_Id = self.__cloudRegion + ":" + instance_Id
                request_headers = {'Content-Type': 'application/json', 'X-ApiKey': self.__apiKey, 'X-CorrelationId': correltion_Id, 'X-CloudRegion': self.__cloudRegion}           
                response = requests.delete(self.__url, data = json.dumps(eventMessage), headers=request_headers, verify=False)  # TODO - set verify=True after get valid cert

            except requests.exceptions.RequestException as ex:
                self.__logger.exception(ex)
                return False
        
            self.__logger.info("")
            result = json.loads(response.text)
            self.__logger.info(json.dumps(result, indent = 4))

            if response.status_code == 200:
                return True

            elif response.status_code == 404 or response.status_code == 400:  # Check to see if Bad Request and  Not Found 
                return True

            else:
                self.__logger.error("\n deprovisionServer() returned an error %s, the response is:\n%s" % (response.status_code, response.text))
                return None


    def handleEvent(self, body):

        message = json.loads(body)

        if message.has_key("event_type"):
            self.__logger.info('event_type: ' + message["event_type"])
            print ('')

            if message["event_type"] == 'compute.instance.create.end':
                self.__printMessage(message)
                return self.__provisionServer(message)

            elif message["event_type"] == 'compute.instance.delete.end':
                self.__printMessage(message)
                return self.__deprovisionServer(message)

            else:
                return None
