#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.invoiceState import invoiceState
from case.public.oprateTime import oprationTime
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class incomeRechord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test026_incomeRecord(self):
        u"""收入记录"""
        driver.find_element_by_link_text(u"收入记录").click()
        sleep(5)

    def test027_cardID(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("200100008896")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test028_identificationNu(self):
        u"""纳税人识别号"""
        driver.find_element_by_id("taxpayerIdentificationNumber").send_keys("911101083180097938")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_element_by_id("taxpayerIdentificationNumber").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test029_invoiceState(self):
        u"""按发票状态查询"""
        iv = invoiceState()
        iv.invoiceState()

    def test030_operateTime(self):
        u"""按操作时间查询"""
        op = oprationTime()
        op.oprationTime()

    def test031_pageDisplay(self):
        u"""翻页检查"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test032_numDisplay(self):
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
    unittest.main