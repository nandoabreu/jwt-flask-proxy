#! /usr/bin/env python3
'''
SQLite3 database creation and structure

This script runs when requested by proxy.
If this module is called, it will create a new db if none exists.
To configure SQLite3 file location, use config.py.

For instructions, see: https://github.com/nandoabreu/jwt-flask-proxy
'''

import os
import sqlite3
from sqlite3 import Error
import logging
from proxy import config as cfg


def _store(conn, action='process') -> int:
    '''
    Increment the number of requests

    Argument:
        action (str): As in 'process' or 'respond'

    Return:
        int: increased counter
    '''
    query = f'INSERT OR REPLACE INTO requests (action, counter) VALUES ( \
                {action!r}, COALESCE((SELECT counter FROM requests WHERE action = {action!r}),0)+1 \
            )'
    logging.debug(f'SQL: {query[:40]!r}...')

    try:
        cur = conn.execute(query)
        conn.commit()
    except Error as e:
        logging.warning(e)

    return requests(conn, action)

def requests(conn, action='process') -> int:
    '''
    Return number of requests
    If a username is informed, filter the response

    Argument:
        action (str): As in 'process' or 'respond'

    Return:
        int: number of requests
    '''
    query = f'SELECT COALESCE((SELECT counter FROM requests WHERE action = {action!r}),0)'
    cur = conn.execute(query)

    logging.debug(f'SQL: {query[:40]!r}...')
    return cur.fetchone()[0]

def connect():
    '''
    Create database connection with file set in config.py

    The function requests validation of the sqlite_file
    and creates path, database and tables if not exist.
    '''
    conn = None
    _verify_database_file()

    try:
        logging.info(f'Connect to SQLite {sqlite3.version} in {cfg.sqlite_file!r}')
        conn = sqlite3.connect(cfg.sqlite_file)
    except Error as e:
        logging.critical(e)

    _verify_database_tables(conn)
    return conn

def _verify_database_tables(conn):
    '''Verify [and create] database structure'''

    try:
        cur = conn.execute('SELECT * FROM requests LIMIT 1')
        logging.debug(f'Database exists in: {cfg.sqlite_file!r}...')
    except Error:
        cur = conn.cursor()
        logging.info(f'Create database in: {cfg.sqlite_file!r}...')
        cur.execute('CREATE TABLE requests (action TEXT NOT NULL, counter INT DEFAULT 0, UNIQUE(action))')

def _verify_database_file():
    '''Verify [and create] path to sqlite_file'''
    db_file_path = os.path.split(cfg.sqlite_file)[0]
    if not os.path.isdir(db_file_path):
        logging.warning(f'Creating path to {cfg.sqlite_file!r}...')
        os.makedirs(db_file_path, mode=0o777)


if __name__ == "__main__":
    logging.basicConfig(level=cfg.log_level)
    logging.info("Attempt to connect to SQLite3 in {}".format(cfg.sqlite_file))

    conn = connect()
    if conn: conn.close()

