#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class strategyManagement(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test133_strategyManagement(self):
        u"""计费策略管理"""
        driver.find_element_by_link_text(u"设备管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"计费策略管理").click()
        sleep(2)

    def test134_strategyName(self):
        u"""策略名称"""
        driver.find_elements_by_class_name("textInput")[0].send_keys(u"京汉旭城计费策略")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)

        #查看计费策略详情
        driver.find_element_by_link_text(u"京汉旭城计费策略").click()
        sleep(3)
        #返回
        driver.find_element_by_link_text(u"返回").click()
        sleep(2)

    def test135_add(self):
        u"""添加"""

    def test136_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test137_numberDisplay(self):
        u"""设置每页显示条数"""
        num = numberDisplay()
        num.numberDisplay()
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