#! /usr/bin/env python3
'''
Project's configuration file
*** This file must be renamed to config.py***

This file holds necessary variables to this project.

Algorithm and Secret key:
    ALGO (string): Algorithm to use (HS512)
    SECRET_KEY = 'my-secret-key'

Log variables:
    log_level (str): Use one of CRITICAL, ERROR, WARNING, INFO, DEBUG
    log_path (str): Relative or absolute path to the logs directory
    log_file (str): log filename to record in log_path
    log_response (str): filename to log responses from the endpoint

Endpoint URL:
    endpoint_url (str): URL to the endpoit (dummy) server

Database variables:
    sqlite_file (str): Relative or absolute path to SQLite3 database
'''

# Algorithm and Secret key:
ALGO = 'HS512'
SECRET_KEY = 'my-secret-key'

# Log variables:
log_level = 'DEBUG'
log_path = 'logs'
log_file = 'project.log'
log_response = 'endpoint.log'

# Endpoint URL:
endpoint_url = 'https://postman-echo.com/post'

# SQLite3 config:
sqlite_file = 'data/sqlite.db'



# From this line, code to create
# the log_path defined in 'log_path'

import os
if not os.path.exists(log_path):
    os.makedirs(log_path)

