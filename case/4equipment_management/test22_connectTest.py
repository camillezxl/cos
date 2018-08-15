#coding:utf-8
import unittest
from config.config import config
from time import sleep

driver = config.driver
class connectTest(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test145_connectTest(self):
        u"""测试连接"""
        driver.find_element_by_link_text(u"设备管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"测试连接").click()
        sleep(2)

    def test146_productionConnect(self):
        u"""生产连接"""
        driver.find_element_by_link_text(u"生产测试连接").click()
        sleep(2)
        driver.find_element_by_xpath(".//*[@id='alertMsgBox']/div[1]/div/div[2]/ul/li/a").click()
        sleep(2)

    def test147_grayConnect(self):
        u"""灰度连接"""
        driver.find_element_by_link_text(u"灰度测试连接").click()
        sleep(2)
        driver.find_element_by_xpath(".//*[@id='alertMsgBox']/div[1]/div/div[2]/ul/li/a").click()
        sleep(2)


if __name__ == '__main__':
    unittest.main()