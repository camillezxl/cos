#coding:utf-8
import unittest
from config.config import config
from time import sleep
from selenium.webdriver.support.select import Select
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class invoiceRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test033_invoiceRecord(self):
        u"""发票记录"""
        driver.find_element_by_link_text(u"发票记录").click()
        sleep(2)

    def test034_cardID(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("200100010591")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test035_texpayerID(self):
        u"""按纳税人识别号查询"""
        driver.find_element_by_id("taxpayerIdentificationNumber").send_keys("911101083398496604")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_element_by_id("taxpayerIdentificationNumber").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test036_invoiceState(self):
        u"""按发票状态查询"""
        for i in range(1,5):
            s = driver.find_element_by_id("invoiceYpe")
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(2)
        s = driver.find_element_by_id("invoiceYpe")
        Select(s).select_by_value("")
        sleep(2)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)

    def test037_invoiceCode(self):
        u"""按发票代码查询"""
        driver.find_elements_by_class_name("textInput")[2].send_keys("02701361-1100171320")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)
        driver.find_elements_by_class_name("textInput")[2].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)

    def test038_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test039_numberDisplay(self):
        u"""每页展示条数"""
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