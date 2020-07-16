#! /usr/bin/env python3
'''
Python HTTP Proxy

Usage:
    $ python3 -m dog

'''

SECRET_KEY = 'soon'
ALGO = 'HS512'

from flask import Flask
from flask import request
from flask import make_response, jsonify
import datetime
import jwt
from json import dumps
#import base64
import hashlib


app = Flask(__name__)
app.debug = False

@app.route('/auth', methods=['POST'])
def auth():
    if not request.json or not 'user' in request.json:
        return bad_request()

    now = datetime.datetime.utcnow()
    user = request.json['user']

    headers = {'alg': ALGO, 'typ': 'JWT'}
    pldata = {'iat': int(now.timestamp()),
              'exp': int((now + datetime.timedelta(seconds=3600)).timestamp()),
              'jti': hashlib.md5(f'{user}{now.timestamp()}'.encode('utf8')).hexdigest(),
              'user': user, 
              'date': now.strftime('%F')}

    access_token = jwt.encode(pldata, SECRET_KEY, algorithm=ALGO, headers=headers).decode('utf8')
    return jsonify({'access_token': access_token})

@app.route('/')
def index():
    return "Hello, castLabs!"

def bad_request():
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    app.run()

