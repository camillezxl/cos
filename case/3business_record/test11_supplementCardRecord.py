#coding:utf-8
import unittest
from time import sleep
from config.config import config
from case.public.oprateTime import oprationTime
from case.public.export import export
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class supplementCardRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test067_supplementCardRecord(self):
        u"""补卡记录"""
        driver.find_element_by_link_text(u"业务记录").click()
        sleep(1)
        driver.find_element_by_link_text(u"补卡记录").click()
        sleep(3)

    def test068_cardID(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("200100012396")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test069_holderID(self):
        u"""按持卡人身份证查询"""
        driver.find_elements_by_class_name("textInput")[1].send_keys("35212119620805008X")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test070_oprateTime(self):
        u"""按操作时间查询"""
        op = oprationTime()
        op.oprationTime()

    def test071_export(self):
        u"""导出列表"""
        et = export()
        et.export()

    def test072_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test073_numDisplay(self):
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