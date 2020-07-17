#! /usr/bin/env python3
'''Package for the HTTP proxy server to generate JWT (JSON Web Tokens)'''

import os
import logging
from proxy import config as cfg


# logging hack in case of windows
datefmt = '%Y%m%dT%H%M%S' if os.name == 'nt' else '%s'

# Set log level and path in config
log_file = os.path.join(cfg.log_path, cfg.log_file)
logging.basicConfig(level=cfg.log_level, filename=log_file, datefmt='%s',
                    format='%(asctime)s:%(levelname)s:%(message)s')

