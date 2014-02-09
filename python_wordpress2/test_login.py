# -*- coding: cp936 -*-

import unittest
from selenium import webdriver
import time
import login


class WordPressTestCase(unittest.TestCase):
    dr = None

    def setUp(self):
        self.dr = webdriver.Firefox()
        
    def test_login(self):
        con = login.commen(self.dr)
        con.login()
        print self.dr.current_url
        self.assertTrue('wp-admin' in self.dr.current_url)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()
