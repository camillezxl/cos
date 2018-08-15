#coding:utf-8
import unittest
from config.config import config
from time import sleep
from selenium.webdriver.support.select import Select
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class warehouseManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test182_warehouseManagement(self):
        u"""入库管理"""
        driver.find_element_by_link_text(u"卡管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"入库管理").click()
        sleep(2)

    def test183_cardNum(self):
        u"""卡号"""
        driver.find_element_by_id("cardCode").send_keys("200100010508")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)
        driver.find_element_by_link_text(u"修改").click()
        sleep(2)
        driver.find_elements_by_class_name("buttonActive")[1].click()
        sleep(2)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)

    def test184_cardState(self):
        u"""发卡状态"""
        for i in range(1,3):
            s = driver.find_element_by_id("cardStatus")
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(2)

        s = driver.find_element_by_id("cardStatus")
        Select(s).select_by_index(0)
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)

    def test185_warehouse(self):
        u"""入库"""
        driver.find_element_by_link_text(u"入库").click()
        sleep(2)
        driver.find_elements_by_class_name("buttonActive")[1].click()
        sleep(2)

    def test186_writeCard(self):
        u"""写卡"""
        driver.find_element_by_link_text(u"写卡").click()
        sleep(2)
        driver.find_elements_by_class_name("buttonActive")[0].click()
        sleep(2)

    def test187_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test188_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()

if __name__ == '__main__':
    unittest.main()