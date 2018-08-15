#coding:utf-8
import unittest
from time import sleep
from config.config import config
from case.public.oprateTime import oprationTime
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class chargeChangeRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test040(self):
        u"""充值变更记录"""
        driver.find_element_by_link_text(u"充值变更记录").click()
        sleep(2)

    def test041(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("200100010591")
        sleep(1)
        for i in range(2):
            driver.find_elements_by_class_name("button")[1].click()
            sleep(2)


    def test042(self):
        u"""按原流水号查询"""
        driver.find_elements_by_class_name("textInput")[1].send_keys("20180615152704545643152")
        sleep(1)
        for i in range(2):
            driver.find_elements_by_class_name("button")[1].click()
            sleep(2)

    def test043(self):
        u"""按操作时间查询"""
        ot = oprationTime()
        ot.oprationTime()

    def test044(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test045(self):
        u"""每页显示条数"""
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
