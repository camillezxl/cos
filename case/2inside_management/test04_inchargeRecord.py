#coding:utf-8
import unittest
from time import sleep
from config.config import config
from case.public.oprateTime import oprationTime
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class insideChargeRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test013_insideRecord(self):
        u"""内部充值记录"""
        driver.find_element_by_link_text(u"内部管理").click()
        sleep(2)
        driver.find_element_by_link_text(u"内部充值记录").click()
        sleep(2)

    def test014_card(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("200100007150")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)
        driver.find_element_by_id("cardCode").clear()
        sleep(2)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)

    def test015_time(self):
        u"""按操作时间查询"""
        op = oprationTime()
        op.oprationTime()

    def test016_pageDisplay(self):
        u"""翻页检查"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test017_numberDisplay(self):
        u"""按每页显示条数查询"""
        nd = numberDisplay()
        nd.numberDisplay()
        num = driver.find_element_by_partial_link_text("10").text
        print(num)
        text = "10"
        if num==text:
            pass
        else:
            print(u"每页显示10条出现异常")
            self.assertFalse(text)
if __name__ == '__main__':
    unittest.main()