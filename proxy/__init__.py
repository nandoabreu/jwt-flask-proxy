#! /usr/bin/env python3
'''
Package for the HTTP proxy server to generate JWT (JSON Web Tokens)

This app requires:
    python 3.6+
    Flask
    PyJWT
    urllib3

Endpoints:
    / (GET): Request a new JSON Web Token using form and AJAX
    /auth (POST): Generate the JWT
    /status (GET): Status of this proxy

Setup:
    $ python3 -m proxy
'''

import os
import logging
from proxy import config as cfg


# logging hack in case of windows
_datefmt = '%Y%m%dT%H%M%S' if os.name == 'nt' else '%s'

# Set log level and path in config
_log_file = os.path.join(cfg.log_path, cfg.log_file)
logging.basicConfig(level=cfg.log_level, filename=_log_file, datefmt=_datefmt,
                    format='%(asctime)s:%(levelname)s:%(message)s')

