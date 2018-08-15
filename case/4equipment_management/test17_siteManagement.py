#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay
from case.public.export import export

driver = config.driver
class siteManagement(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test119_siteManagement(self):
        u"""站点管理"""
        driver.find_element_by_link_text(u"设备管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"站点管理").click()
        sleep(3)

    def test120_siteCode(self):
        u"""站点编号"""
        driver.find_elements_by_class_name("textInput")[0].send_keys("PDHTQCXS")
        for i in range(2):
            driver.find_elements_by_class_name("button")[0].click()
            sleep(2)

    def test121_siteName(self):
        u"""站点名称"""
        driver.find_elements_by_class_name("textInput")[1].send_keys(u"万丰小吃城充电站")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)

        driver.find_element_by_link_text(u"万丰小吃城充电站").click()
        sleep(2)

        js = "document.getElementById('mainContent').scrollTop=10000"
        driver.execute_script(js)
        sleep(2)
        #末页
        driver.find_element_by_link_text(u"末页").click()
        sleep(3)

        #首页
        driver.find_element_by_link_text(u"首页").click()
        sleep(3)
        driver.execute_script(js)
        sleep(2)

        nd = numberDisplay()
        nd.numberDisplay()

        driver.find_element_by_link_text(u"返回").click()
        sleep(2)

    def test122_extport(self):
        u"""导出"""
        et = export()
        et.export()

    def test123_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test124_numberDisplay(self):
        u"""设置每页显示条数"""
        bnd = numberDisplay()
        bnd.numberDisplay()

        driver.find_element_by_link_text(u"万丰小吃城充电站").click()
        sleep(2)

        #查看充电桩详情
        driver.find_elements_by_link_text(u"详情")[0].click()
        sleep(2)
        js = "document.getElementsByClassName('pageFormContent')[0].scrollTop=10000"
        driver.execute_script(js)
        sleep(2)

        js = "document.getElementsByClassName('pageFormContent')[0].scrollTop=0"
        driver.execute_script(js)
        sleep(2)

        #查看该充电桩充电记录
        driver.find_element_by_link_text(u"充电记录").click()
        sleep(2)

        #导出充电记录
        cet = export()
        cet.export()

        #检查翻页
        dpd = pageDisplay()
        dpd.pageDisplay()

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
        sleep(2)

if __name__ == '__main__':
    unittest.main()