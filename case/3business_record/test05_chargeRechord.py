#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.oprateTime import oprationTime
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class chargeRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test018_chargeRecord(self):
        u"""充值记录"""
        driver.find_element_by_link_text(u"业务记录").click()
        sleep(2)
        driver.find_element_by_link_text(u"充值记录").click()
        sleep(5)

    def test019_cardID(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("200100008896")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test020_name(self):
        u"""按会员姓名查询"""
        driver.find_elements_by_class_name("textInput")[1].send_keys(u"叶丽娜")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test021_phone(self):
        u"""按会员电话查询"""
        driver.find_elements_by_class_name("textInput")[2].send_keys("13671158183")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[2].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test022_ID(self):
        u"""按会员证件号查询"""
        driver.find_elements_by_class_name("textInput")[3].send_keys("37292219800418621X")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[3].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test023_time(self):
        u"""按操作时间查询"""
        op = oprationTime()
        op.oprationTime()

    def test024_pageDisplay(self):
        u"""翻页检查"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test025_numDisplay(self):
        u"""按每页显示条数查询"""
        nd = numberDisplay()
        nd.numberDisplay()
        sleep(3)
        num = driver.find_elements_by_partial_link_text("10")[0].text
        print(num)
        text = "10"
        if num==text:
            pass
        else:
            print(u"每页显示10条出现异常")
            self.assertFalse(text)

if __name__ == '__main__':
    unittest.main()