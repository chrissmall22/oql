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

import os
from setuptools import setup
from pip.req import parse_requirements

# Get version from hpsdclient.version in a PY3 safe manner



def requires(filename):
    requirements = parse_requirements(os.path.abspath(filename))
    return [str(r.req) for r in requirements]


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='oql',
    version='0.1',  # pylint: disable E0602
    description=("A python library to make interacting with the"
                 "Openstack Messaging Queues"),
    long_description=readme(),
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['hpe', 'openstack', 'rabbitmq'],
    url='https://github.com/chissmall22/odl',
    author="Chris Small, Hewlett-Packard Development Company, L.P",
    author_email="christopher.small@hpe.com",
    license='Apache License, Version 2.0',
    packages=['oql'],
    include_package_data=True,
    install_requires=requires('requirements.txt'),
    test_suite='nose.collector',
    tests_require=requires('test-requirements.txt'),
    zip_safe=False,
)