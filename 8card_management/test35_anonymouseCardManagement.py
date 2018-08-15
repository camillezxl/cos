#coding:utf-8
import unittest,time
from config.config import config
from time import sleep
from case.public.export import export
from case.public.numberDisplay import numberDisplay
from case.public.receiveState import receiveState
from case.public.pageDisplay import pageDisplay
from selenium.webdriver.support import expected_conditions as EC

driver = config.driver
class anonymouseCardManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test220_anonymouseCardManagement(self):
        u"""不记名卡管理"""
        driver.find_element_by_link_text(u"卡管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"不记名卡管理").click()
        sleep(3)
        try:
            lactor = ("id","receiveStatus")
            text = u"全部"
            result = EC.text_to_be_present_in_element(lactor,text)(driver)
            self.assertTrue(result)

        except Exception as msg:
            print(u"异常原因%s"%msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            driver.get_screenshot_as_file("E:\\Python\\cos\\png\\%s.jpg"%nowTime)
            driver.find_element_by_link_text(u"确定").click()
            sleep(2)
            driver.find_element_by_link_text(u"不记名卡管理").click()
            sleep(2)
            self.assertFalse(nowTime)
            raise

    def test221_cardID(self):
        u"""卡号"""
        driver.find_elements_by_class_name("textInput")[0].send_keys("AA9000000423")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        driver.find_element_by_link_text(u"详情").click()
        sleep(5)
        try:
            lactor = ("xpath",".//*[@id='mainContent']/div/dl[4]/dt[3]/label")
            text = u"折扣"
            result = EC.text_to_be_present_in_element(lactor,text)
            self.assertTrue(result)
            bnu = numberDisplay()
            bnu.numberDisplay()

        except Exception as msg:
            print(u"异常原因%s"%msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            driver.get_screenshot_as_base64("E:\\Python\\cos\\png\\%s.jpg"%nowTime)
            self.assertFalse(nowTime)
            raise

    def test222_receiveState(self):
        u"""领取状态"""
        driver.find_element_by_link_text(u"不记名卡管理").click()
        sleep(2)
        rs = receiveState()
        rs.receiveState()

    def test223_cardBeloneToEnterprise(self):
        u"""卡归属企业"""
        driver.find_elements_by_class_name("textInput")[1].send_keys(u"富电新能源")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)

    def test224_export(self):
        u"""导出"""
        et = export()
        et.export()

    def test225_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test226_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()


if __name__ == '__main__':
    unittest.main()