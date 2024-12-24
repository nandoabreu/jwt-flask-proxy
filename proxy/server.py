#! /usr/bin/env python3

from flask import Flask
from flask import request
from flask import make_response, jsonify
from flask import render_template as rt
from os import path
import requests
import datetime
import logging
from proxy import config as cfg
from proxy.Token import Token
from proxy import db


_app = Flask(__name__)
_app.debug = True
uptime = datetime.datetime.utcnow()

@_app.route('/auth', methods=['POST'])
def auth():
    '''
    Create JWT and upstream

    Argument:
        user (str): username (as an e-mail)
    '''
    conn = db.connect()
    count = db._store(conn)

    if request.json: logging.debug(f'I got {request.json}')
    if not request.json or not 'user' in request.json:
        logging.warning(f'No request or no attribute user')
        return _bad_request()

    user = request.json['user']

    logging.debug(f'Call Token for {user!r}')
    token = Token(user)

    upstream = { 'Authorization': token.jwt }
    res = requests.post(cfg.endpoint_url, headers=upstream)
    with open(path.join(cfg.log_path, cfg.log_response), 'a') as f:
        f.write(f'status: {res.status_code}\n')
        f.write(f'headers: {res.headers}\n')
        f.write(f'data: {res.text}\n')

    logging.info(f'Respond Token for {user!r}')
    return jsonify({'token': token.jwt})

@_app.route('/')
def index():
    '''Default home page'''
    return rt('index.html', uptime=uptime)

@_app.route('/status')
def status():
    '''Proxy status'''
    conn = db.connect()
    processed = db.requests(conn)
    now = datetime.datetime.utcnow()
    return rt('status.html', uptime=uptime, now=now, processed=processed)

def _bad_request():
    return make_response(jsonify({'error': 'Bad Request'}), 400)

def main():
    _app.run(host=cfg.http_host, port=cfg.http_port)


if __name__ == '__main__':
    main()

