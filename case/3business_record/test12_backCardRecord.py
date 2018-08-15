#coding:utf-8
import unittest
from time import sleep
from config.config import config
from case.public.oprateTime import oprationTime
from case.public.export import export
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class backCardRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test074_backCardRecord(self):
        u"""退卡记录"""
        driver.find_element_by_link_text(u"业务记录").click()
        sleep(1)
        driver.find_element_by_link_text(u"退卡记录").click()
        sleep(3)

    def test075_cardID(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("200100011195")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test076_oprateTime(self):
        u"""按申请时间查询"""
        op = oprationTime()
        op.oprationTime()

    def test077_export(self):
        u"""导出列表"""
        et = export()
        et.export()

    def test078_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test079_numberDisplay(self):
        u"""设置每页显示条数"""
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