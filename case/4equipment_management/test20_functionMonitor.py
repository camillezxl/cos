#coding:utf-8
import unittest
from config.config import config
from time import sleep
from selenium.webdriver.support.select import Select

driver = config.driver
class functionMonitor(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test138_functionMonitor(self):
        u"""运行监控"""
        driver.find_element_by_link_text(u"设备管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"运行监控").click()
        sleep(2)

    def test139_city(self):
        u"""按城市查询"""
        s = driver.find_element_by_id("provinceCode")
        Select(s).select_by_index(1)
        sleep(2)
        s1 = driver.find_element_by_id("cityCode")
        Select(s1).select_by_index(1)
        sleep(2)
        for i in range(1,4):
            s2 = driver.find_element_by_id("siteId")
            Select(s2).select_by_index(i)
            sleep(2)

            driver.find_elements_by_class_name("button")[0].click()
            sleep(3)


if __name__ == '__main__':
    unittest.main()