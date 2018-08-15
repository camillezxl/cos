#coding:utf-8
import unittest
from config.config import config
from time import sleep
from selenium.webdriver.support.select import Select
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class guaranteeRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test148_guaranteeRecord(self):
        u"""报修记录"""
        driver.find_element_by_link_text(u"设备管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"报修记录").click()
        sleep(2)

    def test149_guaranteePhone(self):
        u"""报修人手机号"""
        driver.find_elements_by_class_name("textInput")[0].send_keys("15201529620")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        #查看报修详情
        driver.find_element_by_link_text(u"查看报修").click()
        sleep(3)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)

    def test150_guranteeState(self):
        u"""报修状态"""
        for i in range(1,4):
            s = driver.find_element_by_id("repairStatus")
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[0].click()
            sleep(2)
        s = driver.find_element_by_id("repairStatus")
        Select(s).select_by_index(0)
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)


    def test151_oprateTime(self):
        u"""操作时间"""
        #开始时间
        #去掉readonly属性
        js = "document.getElementsByClassName('date')[0].removeAttribute('readonly');"
        driver.execute_script(js)
        #用js方法输入日期
        startTime = "document.getElementsByClassName('date')[0].value='2018-08-08 00:00:00'"
        driver.execute_script(startTime)
        #结束时间
        #去掉readonly属性
        js = "document.getElementsByClassName('date')[1].removeAttribute('readonly');"
        driver.execute_script(js)
        #用js方法输入日期
        endTime = "document.getElementsByClassName('date')[1].value='2018-08-13 00:00:00'"
        driver.execute_script(endTime)
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(5)
        num = driver.find_element_by_xpath(".//*[@id='mainContent']/div[2]/div[3]/div[1]/span[2]").text
        text = u"条，共 0条"
        if num==text:
            print(u"筛选异常：对应时间有报修记录，但筛选结果无内容")
            #去掉readonly属性
            js = "document.getElementsByClassName('date')[0].removeAttribute('readonly');"
            driver.execute_script(js)
            #用js方法输入日期
            js_value = "document.getElementsByClassName('date')[0].value=''"
            driver.execute_script(js_value)
            #结束时间
            #去掉readonly属性
            js = "document.getElementsByClassName('date')[1].removeAttribute('readonly');"
            driver.execute_script(js)
            #用js方法输入日期
            js_value = "document.getElementsByClassName('date')[1].value=''"
            driver.execute_script(js_value)
            sleep(1)
            driver.find_elements_by_class_name("button")[0].click()
            sleep(5)
            return self.assertFalse(text)
        else:
            pass

    def test152_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test153_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()
        num = driver.find_element_by_partial_link_text("10").text
        print(num)
        text = "10"
        if num==text:
            pass
        else:
            self.assertFalse(text)


if __name__ == '__main__':
    unittest.main()