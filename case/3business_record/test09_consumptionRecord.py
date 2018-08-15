#coding:utf-8
import unittest,time
from time import sleep
from config.config import config
from case.public.settlementState import settlementState
from case.public.settlementMode import settlementMode
from case.public.oprateTime import oprationTime
from selenium.webdriver.support.select import Select
from case.public.signMode import signMode

driver = config.driver
class consumptionRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test046_consumptionRecord(self):
        u"""消费记录"""
        driver.find_element_by_link_text(u"业务记录").click()
        sleep(1)
        driver.find_element_by_link_text(u"消费记录").click()
        sleep(60)

    def test047_cardID(self):
        u"""按卡号查询"""
        driver.find_element_by_id("cardCode").send_keys("AA0000039557")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test048_name(self):
        u"""按会员姓名查询"""
        driver.find_elements_by_class_name("textInput")[1].send_keys("18310176158")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test049_phone(self):
        u"""按会员电话查询"""
        driver.find_elements_by_class_name("textInput")[2].send_keys("18310176158")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[2].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test050_orderState(self):
        u"""按订单结算状态查询"""
        st = settlementState()
        st.settlementState()

    def test051_machineCode(self):
        u"""按终端机器编码查询"""
        driver.find_elements_by_class_name("textInput")[3].send_keys("1020150908001023")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[3].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test052_organizationName(self):
        u"""按机构名称查询"""


    def test053_documentID(self):
        u"""按证件号查询"""
        driver.find_elements_by_class_name("textInput")[4].send_keys("14010919901119554X")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[4].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test054_settlementMethod(self):
        u"""按结算方式查询"""
        sm = settlementMode()
        sm.settlementMode()

    def test055_oprateTime(self):
        u"""按操作时间查询"""
        ot = oprationTime()
        ot.oprationTime()

    def test056_siteName(self):
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

    def test057_signMode(self):
        u"""按签权方式查询"""
        sm = signMode()
        sm.signMode()

    def test058_orderNum(self):
        u"""按订单号查询"""
        driver.find_elements_by_class_name("textInput")[7].send_keys("11321010100002241807311553402922")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[7].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)

    def test059_export(self):
        u"""导出"""
        driver.find_element_by_partial_link_text(u"导出").click()
        sleep(7)
        driver.find_element_by_xpath(".//*[@id='images']/li/a/img").click()
        sleep(5)
        driver.find_elements_by_class_name("buttonActive")[0].click()
        sleep(2)

    def test060_pageDisplay(self):
        u"""检查翻页"""

    def test061_numDisplay(self):
        u"""每页显示条数"""
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(2)
        index = [20,50,100]
        for i in index:
            driver.find_element_by_link_text(i).click()
            sleep(3)
            js = "document.getElementsByClassName('tableList')[0].scrollTop = 10000"
            driver.execute_script(js)
            sleep(5)
            s = driver.find_element_by_link_text(i)
            s.click()
            sleep(5)
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(5)
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