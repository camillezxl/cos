#coding:utf-8
import unittest
from config.config import config
from time import sleep

driver = config.driver
class memberRegistor(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test169_memberRegistor(self):
        u"""会员注册"""
        driver.find_element_by_link_text(u"会员管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"会员注册").click()
        sleep(2)

if __name__ == '__main__':
    unittest.main()