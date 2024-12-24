#! /usr/bin/env python3
'''
Token class module

This module can be imported and used outside the HTTP proxy.
'''
import datetime
import hashlib
import jwt
from proxy import config as cfg


class Token:
    '''
    Token class to generate JWT (JSON Web Token)

    Argument:
        user (string): payload username

    Attribute:
        jwt (string): generated token

    See https://github.com/nandoabreu/jwt-flask-proxy for instructions.
    '''
    def __init__(self, user):
        now = datetime.datetime.utcnow()

        headers = {'alg': cfg.ALGO, 'typ': 'JWT'}
        pldata = {'iat': int(now.timestamp()),
                  'exp': int((now + datetime.timedelta(seconds=3600)).timestamp()),
                  'jti': hashlib.md5(f'{user}{now.timestamp()}'.encode('utf8')).hexdigest(),
                  'user': user,
                  'date': now.strftime('%F')}

        self.jwt = jwt.encode(pldata,
                              cfg.SECRET_KEY, algorithm=cfg.ALGO,
                              headers=headers)

