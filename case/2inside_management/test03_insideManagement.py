#coding:utf-8
import unittest
from time import sleep
from config.config import config
from selenium.webdriver.support.select import Select
from case.public.numberDisplay import numberDisplay
from case.public.pageDisplay import pageDisplay

driver = config.driver
class insideManagement(unittest.TestCase):
    u"""内部管理"""
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test003_insideCharge(self):
        u"""内部充值"""
        driver.find_element_by_link_text(u"内部管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"内部充值").click()
        sleep(3)

    def test004_cardType(self):
        u"""按卡类型搜索"""
        for i in range(1,3):

            s = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[1]/td[1]/select")
            sleep(1)
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(5)

    def test005_cardGroup(self):
        u"""按卡组名称搜索"""
        for i in range(3,6):
            s = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[1]/td[2]/select")
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(5)

    def test006_cardNum(self):
        u"""按卡号搜索"""
        driver.find_element_by_id("cardCode").send_keys("200100008888")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test007_cardState(self):
        u"""按卡状态搜索"""
        for i in range(1,5):
            s = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[1]/select")
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(5)

    def test008_cardHolder(self):
        u"""根据持卡人查询"""
        driver.find_elements_by_class_name("textInput")[1].send_keys(u"李晓刚")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test009_ID(self):
        u"""根据身份证号码查询"""
        driver.find_elements_by_class_name("textInput")[2].send_keys("130404196102182153")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test010_time(self):
        u"""发卡时间"""
        #去掉readonly属性
        js = "document.getElementsByClassName('date')[0].removeAttribute('readonly');"
        driver.execute_script(js)
        #用js的方法输入日期
        js_value = "document.getElementsByClassName('date')[0].value='2018-07-16'"
        driver.execute_script(js_value)
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        #去掉readonly属性
        js = "document.getElementsByClassName('date')[0].removeAttribute('readonly');"
        driver.execute_script(js)
        #用js的方法输入日期
        js_value = "document.getElementsByClassName('date')[0].value=''"
        driver.execute_script(js_value)
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)


    def test011_pageDisplay(self):
        pd = pageDisplay()
        pd.pageDisplay()

    def test012_numberDisplay(self):
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

