#! /usr/bin/env python3

import unittest
from proxy.Token import Token

verbose_tests = False


class TokenTests(unittest.TestCase):
    def setUp(self):
        self.token = Token('unittest')

    def tearDown(self):
        pass

    def test_object(self):
        self.assertIsInstance(self.token, Token)
        if verbose_tests: print("TEST:ran test_object")

    def test_jwt_len(self):
        self.assertGreater(len(self.token.jwt), 260)
        self.assertLess(len(self.token.jwt), 610)
        if verbose_tests: print("TEST:ran test_jwt_len")

    def test_jwt_content(self):
        self.assertRegex(self.token.jwt, '^eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9\.')
        self.assertRegex(self.token.jwt, '^(.*)\.(.*)\.(.*)$')
        if verbose_tests: print("TEST:ran test_jwt_content")

    def test_new_jwt(self):
        other_jwt = Token('unittest').jwt
        self.assertNotEqual(self.token.jwt, other_jwt)
        if verbose_tests: print("TEST:ran test_new_jwt")


if __name__ == '__main__':
    unittest.main()

