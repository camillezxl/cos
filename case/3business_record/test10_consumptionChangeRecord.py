#coding:utf-8
import unittest
from time import sleep
from config.config import config
from case.public.oprateTime import oprationTime
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class consumptionChangeRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test062_consumptionChangeRecord(self):
        u"""消费变更记录"""
        driver.find_element_by_link_text(u"消费变更记录").click()
        sleep(2)

    def test063_cardID(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("200100008302")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test064_oprationTime(self):
        u"""按操作时间查询"""
        op = oprationTime()
        op.oprationTime()

    def test065_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test066_numberDisplay(self):
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