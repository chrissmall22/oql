#!/usr/bin/env python
import pika
import sys
import conigparser
import argparse
import requests


# Accept options of text or json
parser = argparse.ArgumentParser()
parser.add_argument('--config_file', type=str,
                        help="Type of output to upload",
                        required=False,
                        default='oql.ini')

args = parser.parse_args()

# Get Config Options
config = configparser.ConfigParser()
config.read(config_file)

# Get the default Environment
if config['DEFAULT']['environment']:
  environment = config['DEFAULT']['environment']

if environment and config[environment]['rabbit_host']:
  rabbit_host = config[environment]['rabbit_host']

if environment and config[environment]['rabbit_user']:
  rabbit_user = config[environment]['rabbit_user']

if environment and config[environment]['rabbit_password']:
  rabbit_password = config[environment]['rabbit_password']

if environment and config[environment]['webhook_url']:
  webhook_url = config[environment]['webhook_url']

# Channel Connection 
credentials = pika.credentials.PlainCredentials(username=rabbit_user,
                                                password=rabbit_password,
                                                erase_on_connect=False)

conn_param = pika.ConnectionParameters(host=rabbit_host,
                                       credentials=credentials)
                                               
connection = pika.BlockingConnection(conn_param)
channel = connection.channel()

queue_name = 'notifications.info'

channel.queue_bind(exchange='nova',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

#######################################3

def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    monasca_notif = parce_body(body)
    webhook_send(webhook_url,monasca_notif)


def parce_body(body):
	# TODO: Parce text and return Monasca webhook format
	return body


def webhook_send(webhook_url,notification):
	response = requests.post(
    webhook_url, data=notification,
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to Webhook reciever returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )