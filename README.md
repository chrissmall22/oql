# oql

Openstack Queue Listener

[![Build Status](https://travis-ci.org/chrissmall22/oql.svg?branch=master)](https://travis-ci.org/chrissmall22/oql)
[![Coverage Status](https://coveralls.io/repos/github/chrissmall22/oql/badge.svg?branch=master)](https://coveralls.io/github/chrissmall22/oql?branch=master)

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
