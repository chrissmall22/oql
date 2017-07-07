#!/usr/bin/env python
import pika
import sys
import conigparser
import argparse
# Import Openstack Queue Listener class 
import oql.rabbitmq as listener

config_file = 'rabbit-listener.ini'

# Accept options of text or json
parser = argparse.ArgumentParser()
parser.add_argument('--output', type=str,
                        help="Type of output to upload",
                        required=True)

args = parser.parse_args()
config = listener.get_config(config_file)
conn = listener.get_connection(config)

listener.subscribe(args,config,conn)