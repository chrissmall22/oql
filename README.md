# oql

Openstack Queue Listener

A Tool to listen to a Openstack Notification queues

## Tools 

monitor-simple.py - Simple script to watch the Rabittmq Notification Queue

monitor.py - Will allow many more options in terms of queues, filters, output formats and even message queues other than rabbitmq

To run monitor-simple
'''
monitor-simple.pl [--config_file <ini file>]
'''

Default INI file location is ./oql.ini
 

## Tests

To run unit tests  
'''
tox -e 
'''
