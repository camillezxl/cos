#coding:utf-8
import unittest,time
from time import sleep
from config.config import config
from selenium.webdriver.support.select import Select
from case.public.oprateTime import oprationTime
from selenium.webdriver.support.select import Select
from case.public.numberDisplay import numberDisplay

driver = config.driver
class settlementRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test080_settlementRecord(self):
        u"""结算记录"""
        driver.find_element_by_link_text(u"业务记录").click()
        sleep(1)
        driver.find_element_by_link_text(u"结算记录").click()
        sleep(3)

    def test081_cardID(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("200100007788")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test082_memberName(self):
        u"""按会员姓名查询"""
        driver.find_elements_by_class_name("textInput")[1].send_keys(u"王占国")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test083_phone(self):
        u"""按电话查询"""
        driver.find_elements_by_class_name("textInput")[2].send_keys("17801035198")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_elements_by_class_name("textInput")[2].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test084_settlementState(self):
        u"""按结算状态查询"""
        for i in range(1,5):
            s = driver.find_element_by_id("settlementStatus")
            Select(s).select_by_index(i)
            sleep(2)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(5)

        s = driver.find_element_by_id("settlementStatus")
        Select(s).select_by_value("")
        sleep(2)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test085_certificateID(self):
        u"""按证件号查询"""
        driver.find_elements_by_class_name("textInput")[3].send_keys("410224198405160737")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_elements_by_class_name("textInput")[3].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test086_oprateTime(self):
        u"""按结算时间查询"""
        op = oprationTime()
        op.oprationTime()

    def test087_siteName(self):
        u"""按站点名称查询"""
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

    def test088_pageDisplay(self):
        u"""检查翻页"""
        #滚动条回到底部
        js = "document.getElementsByClassName('layoutBox')[0].scrollTop = 10000"
        #翻页
        for i in range(1):
            driver.execute_script(js)
            sleep(2)
            driver.find_element_by_link_text(u"下一页").click()
            sleep(5)

        #首页
        driver.execute_script(js)
        sleep(3)
        driver.find_element_by_link_text(u"首页").click()
        sleep(5)
        driver.execute_script(js)
        sleep(2)

    def test089_numberDisplay(self):
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

    def test090_export(self):
        u"""导出"""
        driver.find_element_by_partial_link_text(u"导出").click()
        sleep(3)
        driver.find_element_by_xpath(".//*[@id='images']/li[1]/a/img").click()
        sleep(3)
        driver.find_element_by_class_name("buttonActive").click()
        sleep(3)


if __name__ == '__main__':
    unittest.main()