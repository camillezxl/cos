#coding:utf-8
import unittest
from config.config import config
from time import sleep

driver = config.driver
class roleManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test002_roleManagement(self):
        u"""角色管理"""
        driver.find_element_by_link_text(u"角色管理").click()
        sleep(1)
        driver.find_element_by_class_name("textInput").send_keys("test")
        sleep(1)
        driver.find_element_by_class_name("button").click()
        sleep(1)

if __name__ == "__name__":
    unittest.main()