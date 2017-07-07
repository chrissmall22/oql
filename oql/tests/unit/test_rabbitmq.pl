#!/usr/bin/env python
#
#   Copyright 2014 Hewlett-Packard Development Company, L.P.
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

import json
import os
import re
import unittest
#PY3.3
import io
try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock

import httpretty
import requests

import oql.rabbitmq 


class RabbitmqTests(unittest.TestCase):
    def setUp(self):
        self.environment = "test_env"
        self.rabbitmq_user = "test_user"
        self.rabbitmq_password = "test_password"

    def test_rabbitmq_instantiation(self):
        self.assertEqual(self.client.args["environment"], self.environment)
       

    
