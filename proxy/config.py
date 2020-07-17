#! /usr/bin/env python3
'''
Project's configuration file
*** This file must be renamed to config.py***

This file holds necessary variables to this project.

HTTP Proxy server:
    http_host (str): If you wish not to use 0.0.0.0 (all interfaces), please edit
    http_port (int): If you wish not to use port 5000, please edit

Algorithm and Secret key:
    ALGO (str): Algorithm to use (HS512)
    SECRET_KEY (str): Place your secret key

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

# HTTP Proxy server:
http_host = '0.0.0.0'
http_port = 5000

# Algorithm and Secret key:
ALGO = 'HS512'
SECRET_KEY = 'a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01 d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf'

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

