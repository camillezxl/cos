#coding:utf-8
import unittest,time
from config.config import config
from time import sleep
from case.public.export import export
from selenium.webdriver.support.select import Select
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class pileManagement(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test125_pileManagement(self):
        u"""充电桩管理"""
        driver.find_element_by_link_text(u"设备管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"充电桩管理").click()
        sleep(2)

    def test126_pileCode(self):
        u"""充电桩编码"""
        driver.find_elements_by_class_name("textInput")[0].send_keys("A7-006-SZX")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)

        #查看充电桩详情
        driver.find_element_by_link_text("A7-006-SZX").click()
        sleep(2)
        js = "document.getElementsByClassName('pageFormContent')[0].scrollTop=10000"
        driver.execute_script(js)
        sleep(2)

        js = "document.getElementsByClassName('pageFormContent')[0].scrollTop=0"
        driver.execute_script(js)
        sleep(2)

        #查看该充电桩充电记录
        driver.find_element_by_link_text(u"充电记录").click()
        sleep(5)

        #导出充电记录
        cet = export()
        cet.export()

        #设置每页显示条数
        end = numberDisplay()
        end.numberDisplay()
        num = driver.find_element_by_partial_link_text("10").text
        print(num)
        text = "10"
        if num==text:
            pass
        else:
            print(u"每页显示10条出现异常")
            self.assertFalse(text)

        driver.find_element_by_link_text(u"返回").click()
        sleep(5)

    def test127_machineCode(self):
        u"""终端机器编码"""
        driver.find_elements_by_class_name("textInput")[1].send_keys("1322111110005663")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)
        #查看充电桩详情
        driver.find_element_by_link_text("A7-001-SZX").click()
        sleep(2)
        js = "document.getElementsByClassName('pageFormContent')[0].scrollTop=10000"
        driver.execute_script(js)
        sleep(2)

        js = "document.getElementsByClassName('pageFormContent')[0].scrollTop=0"
        driver.execute_script(js)
        sleep(2)

        #查看该充电桩充电记录
        driver.find_element_by_link_text(u"充电记录").click()
        sleep(5)

        #导出充电记录
        cet = export()
        cet.export()

        #设置每页显示条数
        end = numberDisplay()
        end.numberDisplay()

        driver.find_element_by_link_text(u"返回").click()
        sleep(5)


    def test128_siteName(self):
        u"""站点名称"""
        sites = ['1121','109','5']
        texts = [u"中国技术交易大厦",u"华贸城充电站",u"华贸中心写字楼地下停车场充电站"]
        s = driver.find_element_by_id("siteIdDetails")
        Select(s).select_by_value(sites[0])
        sleep(2)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(5)

        print(texts[0])
        result = driver.find_element_by_xpath(".//*[@id='mainContent']/div[2]/div[2]/table/tbody/tr[1]/td[11]").text
        if texts[0]==result:
            self.assertTrue(result)
        else:
            print(u"站点搜索结果错误：仅为中国技术交易大厦")
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            t = driver.get_screenshot_as_file("E:\\Python\\cos\\png\\%s.jpg"%nowTime)
            self.assertFalse(nowTime)

        s = driver.find_element_by_id("siteIdDetails")
        Select(s).select_by_value(sites[1])
        sleep(2)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(5)

        print(texts[1])
        result = driver.find_element_by_xpath(".//*[@id='mainContent']/div[2]/div[2]/table/tbody/tr[1]/td[11]").text
        if texts[1]==result:
            self.assertTrue(result)
        else:
            print(u"站点搜索结果错误：仅为华贸城充电站")
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            t = driver.get_screenshot_as_file("E:\\Python\\cos\\png\\%s.jpg"%nowTime)
            self.assertFalse(nowTime)

        s = driver.find_element_by_id("siteIdDetails")
        Select(s).select_by_value(sites[2])
        sleep(2)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(5)

        print(texts[2])
        result = driver.find_element_by_xpath(".//*[@id='mainContent']/div[2]/div[2]/table/tbody/tr[1]/td[11]").text
        if texts[2]==result:
            self.assertTrue(result)
        else:
            print(u"站点搜索结果错误：仅为华贸中心写字楼地下停车场充电站")
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            t = driver.get_screenshot_as_file("E:\\Python\\cos\\png\\%s.jpg"%nowTime)
            self.assertFalse(nowTime)

        s = driver.find_element_by_id("siteIdDetails")
        Select(s).select_by_index(0)
        sleep(2)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(5)

    def test129_export(self):
        u"""导出"""
        et = export()
        et.export()

    def test130_add(self):
        u"""添加"""

    def test131_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test132_numDisplay(self):
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