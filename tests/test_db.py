#! /usr/bin/env python3

import unittest
from proxy import db

verbose_tests = False


class DbTests(unittest.TestCase):
    def setUp(self):
        self.db = db.connect()

    def tearDown(self):
        self.db.close()

    def test_object(self):
        self.assertIsInstance(self.db, object)
        if verbose_tests: print("TEST:ran test_object")

    def test_requests(self):
        self.assertIsInstance(db.requests(self.db), int)
        if verbose_tests: print("TEST:ran test_requests")


if __name__ == '__main__':
    unittest.main()

