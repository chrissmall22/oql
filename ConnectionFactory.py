#!/usr/bin/env python
import pika
import distutils.util
import json
from optparse import OptionParser


class ConnectionFactory(object):

    queue_name = None
    exchange_name = None
    __channel = None
    __connection = None
    ROUTING_KEY = 'notifications.info'

    def __init__(self, config, logger):

        self.__cloud = config.get('DEFAULT', 'cloud')
        self.__rabbit_host = config.get(self.__cloud, 'rabbit_host')
        self.__rabbit_user = config.get(self.__cloud, 'rabbit_user')
        self.__rabbit_password = config.get(self.__cloud, 'rabbit_password')
        self.__logger = logger
        self.__port = config.get(self.__cloud, 'port')
        self.__ssl = config.get(self.__cloud, 'ssl')
        self.queue_name = config.get(self.__cloud, 'queue_name')
        self.exchange_name = config.get(self.__cloud, 'exchange_name')
        self.wait_time = config.get(self.__cloud, 'wait_time')  # in second
        self.__auto_delete = config.get(self.__cloud, 'auto_delete')


    def createChannel(self):

        self.__logger.info('Connecting to RabbitMQ %s', self.__rabbit_host)

        credentials = pika.PlainCredentials(self.__rabbit_user, self.__rabbit_password)

        portNumber = int(self.__port)
        enableSSL = bool(distutils.util.strtobool(self.__ssl))
        parameters =  pika.ConnectionParameters(self.__rabbit_host, credentials=credentials, heartbeat_interval=600, ssl=enableSSL, port=portNumber, socket_timeout=6000, connection_attempts=10)

        ConnectionFactory.__connection = pika.BlockingConnection(parameters)

        try:

            ConnectionFactory.__channel = ConnectionFactory.__connection.channel()

            ConnectionFactory.__channel.exchange_declare(exchange=self.exchange_name, exchange_type='topic', durable=True, auto_delete=self.__auto_delete) 
            ConnectionFactory.__channel.exchange_bind(destination=self.exchange_name, source='nova', routing_key=self.ROUTING_KEY)
            ConnectionFactory.__channel.exchange_bind(destination=self.exchange_name, source='neutron', routing_key=self.ROUTING_KEY)

            ConnectionFactory.__channel.queue_declare(queue = self.queue_name, durable=True, exclusive=False, auto_delete=self.__auto_delete) 
            ConnectionFactory.__channel.queue_bind(queue = self.queue_name, exchange=self.exchange_name, routing_key=self.ROUTING_KEY)

            return ConnectionFactory.__channel

        except Exception:
            self.__logger.exception("channel exception occurred!")
            return None


    def closeChannel(self):

        try:
            ConnectionFactory.__channel.close()
            ConnectionFactory.__connection.close()
            return True

        except Exception:
            self.__logger.exception("Error occurred while closing the channel!")
            return False
