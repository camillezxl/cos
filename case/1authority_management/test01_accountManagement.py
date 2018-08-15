#coding:utf-8
import unittest,time
from config.config import config
from time import sleep
from logger.logger import Log

log = Log()
driver = config.driver
class accountManagement(unittest.TestCase):
    def setUp(self):
        sleep(2)

    def tearDown(self):
        sleep(2)
        log.info(u"--------测试结束--------")

    def test001_accountManagement(self):
        u"""账号管理"""
        log.info(u"--------测试用例开始--------")
        driver.find_element_by_link_text(u"权限管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"账号管理").click()
        sleep(1)
        driver.find_element_by_class_name("textInput").send_keys("txj_testjg1")
        sleep(1)
        log.info(u"输入内容：txj_testjg1")
        driver.find_element_by_class_name("button").click()
        sleep(2)
        log.info(u"点击按钮：class = button")
        t = driver.title
        log.info(u"获取title的内容：%s"%t)



if __name__ == "__name__":
    unittest.main()