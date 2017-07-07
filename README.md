# oql

Openstack Queue Listener

A Tool to listen to a Openstack Notification queues

## Tools 

__monitor-simple.py__ - Simple script to watch the Rabittmq Notification Queue

__monitor.py__ - Will allow many more options in terms of queues, filters, output formats and even message queues other than rabbitmq

To run monitor-simple
```
monitor-simple.pl [--config_file <ini file>]
```
Default INI file location is ./oql.ini

## Tests

To run unit tests  
```
tox -e 
```
