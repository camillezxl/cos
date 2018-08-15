#coding:utf-8
import unittest
from config.config import config
from time import sleep
from selenium.webdriver.support.select import Select
from case.public.numberDisplay import numberDisplay

driver = config.driver
class activityManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test170_activityManagement(self):
        u"""活动管理"""
        driver.find_element_by_link_text(u"优惠管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"活动管理").click()
        sleep(2)

    def test171_activityName(self):
        u"""活动名称"""
        driver.find_elements_by_class_name("textInput")[0].send_keys(u"万柳服务费活动")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)
        #查看活动详情
        driver.find_elements_by_link_text(u"详情")[2].click()
        sleep(2)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)

    def test172_activityState(self):
        u"""活动状态"""
        for i in range(1,4):
            s = driver.find_element_by_id("flag")
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[0].click()
            sleep(2)
        s = driver.find_element_by_id("flag")
        Select(s).select_by_value('')
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)

    def test173_addActivity(self):
        u"""添加活动"""
        driver.find_element_by_link_text(u"创建活动").click()
        sleep(2)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)

    def test174_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()


if __name__ == '__main__':
    unittest.main()