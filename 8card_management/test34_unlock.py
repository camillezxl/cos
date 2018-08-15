#coding:utf-8
import unittest
from config.config import config
from time import sleep

driver = config.driver
class unlock(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test219_unlock(self):
        u"""解锁"""
        driver.find_element_by_link_text(u"卡管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"解锁").click()
        sleep(2)

if __name__ == '__main__':
    unittest.main()