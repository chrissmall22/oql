#!/usr/bin/env python
#
#   Copyright 2017 Hewlett-Packard Development Company, L.P.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import configparser
import pika


class rabbitmq():
    """This class handles connections to the rabbitmq 
    Openstack message queue"""

    def __init__(self):
        """Initializes the class. Set the server, user and password
        member variables. Sets the token and expiration values to
        None"""
        super(rabbitmq, self).__init__()
        self.environment = "default"
        self.rabbit_host = "localhost"
        self.rabbit_user = None
        self.rabbit_password = None
        self.channel = None

    def get_config(self,config_file):
        config = configparser.ConfigParser()
        config.read(config_file)

        # Get the default Environment
        if config['DEFAULT']['environment']:
            self.environment = config['DEFAULT']['environment']

        if self.environment and config[environment]['rabbit_host']:
            self.rabbit_host = config[self.environment]['rabbit_host']

        if self.environment and config[environment]['rabbit_user']:
            self.rabbit_user = config[self.environment]['rabbit_user']

        if self.environment and config[environment]['rabbit_password']:
            self.rabbit_password = config[self.environment]['rabbit_password']

    def get_connection(self,config):

        # Create Auth Credentials
        credentials = pika.credentials.PlainCredentials(
            username=self.rabbit_user, 
            password=self.rabbit_password, 
            erase_on_connect=False
            )

        conn_param = pika.ConnectionParameters(host=self.rabbit_host,
                                               credentials=credentials)
                                               )
        connection = pika.BlockingConnection(conn_param)
        channel = connection.channel()

        exchange(topic=nova)

        result = channel.queue_declare(queue='notifications.info')




    def subscribe(args,config,conn):
