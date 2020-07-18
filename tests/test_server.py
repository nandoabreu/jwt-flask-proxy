#! /usr/bin/env python3

import unittest
import json
from proxy import server

verbose_tests = False


class ServerTests(unittest.TestCase):
    def setUp(self):
        server._app.testing = True
        self.client = server._app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.mimetype, 'text/html')
        if verbose_tests: print("TEST:ran test_index")

    def test_status(self):
        res = self.client.get('/status')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.mimetype, 'text/html')
        self.assertRegex(res.data, b'this proxy is up')
        self.assertRegex(res.data, b'processed [\d]+ requests')
        if verbose_tests: print("TEST:ran test_status")

    def test_auth_post_empty(self):
        res = self.client.post('/auth')
        self.assertEqual(res.status_code, 400)
        if verbose_tests: print("TEST:ran test_status")

    def test_auth_post_user(self):
        data = {"user": "value"}
        res = self.client.post('/auth', data=json.dumps(data), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertRegex(res.data, b'token')
        if verbose_tests: print("TEST:ran test_auth_post_user")


if __name__ == '__main__':
    unittest.main()

