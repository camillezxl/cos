#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.oprateTime import oprationTime
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class enterpriceManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test163_enerpriceManagement(self):
        u"""企业会员管理"""
        driver.find_element_by_link_text(u"会员管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"企业会员管理").click()
        sleep(2)

    def test164_name(self):
        u"""企业名称"""
        driver.find_elements_by_class_name("textInput")[0].send_keys(u"西安安捷物流有限公司")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)
        #查看详情
        driver.find_element_by_link_text(u"详情").click()
        sleep(2)
        driver.find_element_by_link_text(u"企业会员管理").click()
        sleep(2)

    def test165_cardID(self):
        u"""卡号"""
        driver.find_element_by_id("cardCode").send_keys("200100010977")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        #查看详情
        driver.find_element_by_link_text(u"详情").click()
        sleep(2)
        driver.find_element_by_link_text(u"企业会员管理").click()
        sleep(2)

    def test166_oprateTime(self):
        u"""开户时间"""
        ot = oprationTime()
        ot.oprationTime()

    def test167_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test168_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()
        num = driver.find_element_by_partial_link_text("10").text
        print(num)
        text = "10"
        if num==text:
            pass
        else:
            self.assertFalse(text)
if __name__ == '__main__':
    unittest.main()