#coding:utf-8
import unittest,time
from time import sleep
from config.config import config
from case.public.settlementState import settlementState
from case.public.oprateTime import oprationTime
from selenium.webdriver.support.select import Select
from case.public.signMode import signMode
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class appRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test106_appRecord(self):
        u"""APP消费记录"""
        driver.find_element_by_link_text(u"业务记录").click()
        sleep(1)
        driver.find_element_by_link_text(u"APP消费记录").click()
        sleep(5)

    def test107_cardNum(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("AA0000010686")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test108_memberName(self):
        u"""按会员姓名查询"""
        driver.find_elements_by_class_name("textInput")[1].send_keys(u"莫林恩")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test109_phone(self):
        u"""按电话查询"""
        driver.find_elements_by_class_name("textInput")[2].send_keys("17801035198")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[2].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test110_settlementState(self):
        u"""按结算状态查询"""
        ss = settlementState()
        ss.settlementState()

    def test111_machineCode(self):
        u"""按终端机器编码查询"""
        driver.find_elements_by_class_name("textInput")[3].send_keys("0102016021501278")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[3].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test112_certificatesID(self):
        u"""按证件号码查询"""
        driver.find_elements_by_class_name("textInput")[4].send_keys("450203198612030033")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[4].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test113_oprateTime(self):
        u"""按操作时间查询"""
        op = oprationTime()
        op.oprationTime()

    def test114_siteName(self):
        u"""按站点名称进行查询"""
        sites = ['1121','109','5']
        texts = [u"中国技术交易大厦",u"华贸城充电站",u"华贸中心写字楼地下停车场充电站"]
        s = driver.find_element_by_id("siteId")
        Select(s).select_by_value(sites[0])
        sleep(2)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

        print(texts[0])
        result = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/tbody/tr[1]/td[12]").text
        if texts[0]==result:
            self.assertTrue(result)
        else:
            s = driver.find_element_by_id("siteId")
            Select(s).select_by_value("")
            sleep(2)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(5)
            print(u"站点搜索结果错误：仅为中国技术交易大厦")
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            t = driver.get_screenshot_as_file("E:\\Python\\cos\\png\\%s.jpg"%nowTime)
            self.assertFalse(nowTime)


        s = driver.find_element_by_id("siteId")
        Select(s).select_by_value(sites[1])
        sleep(2)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        print(texts[1])
        result = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/tbody/tr[1]/td[12]").text
        if texts[1]==result:
            self.assertTrue(result)
        else:
            s = driver.find_element_by_id("siteId")
            Select(s).select_by_value("")
            sleep(2)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(5)
            print(u"站点搜索结果错误：仅为华贸城充电站")
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            t = driver.get_screenshot_as_file("E:\\Python\\cos\\png\\%s.jpg"%nowTime)
            self.assertFalse(nowTime)

        s = driver.find_element_by_id("siteId")
        Select(s).select_by_value(sites[2])
        sleep(2)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        print(texts[2])
        result = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/tbody/tr[1]/td[12]").text
        if texts[2]==result:
            self.assertTrue(result)
        else:
            s = driver.find_element_by_id("siteId")
            Select(s).select_by_value("")
            sleep(2)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(5)
            print(u"站点搜索结果错误：仅为华贸中心写字楼地下停车场充电站")
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            t = driver.get_screenshot_as_file("E:\\Python\\cos\\png\\%s.jpg"%nowTime)
            self.assertFalse(nowTime)


    def test115_signMode(self):
        u"""按签权方式进行查询"""
        sim = signMode()
        sim.signMode()

    def test116_export(self):
        u"""导出"""
        driver.find_element_by_partial_link_text(u"导出").click()
        sleep(3)
        driver.find_element_by_xpath(".//*[@id='images']/li[1]/a/img").click()
        sleep(10)
        driver.find_element_by_class_name("buttonActive").click()
        sleep(3)

    def test117_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test118_numberDisplay(self):
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