#! /usr/bin/env python3

import unittest
from proxy import config

verbose_tests = False


class ConfigTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_bind(self):
        self.assertIsInstance(config.http_host, str)
        self.assertIsInstance(config.http_port, int)
        if verbose_tests: print("TEST:ran test_bind")

    def test_algo(self):
        self.assertIn(config.ALGO, ['HS512'])
        self.assertIsInstance(config.SECRET_KEY, str)
        if verbose_tests: print("TEST:ran test_algo")

    def test_endpoint(self):
        self.assertEqual(config.endpoint_url, 'https://postman-echo.com/post')
        if verbose_tests: print("TEST:ran test_endpoint")


if __name__ == '__main__':
    unittest.main()

