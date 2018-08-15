#coding:utf-8
import unittest
from config.config import config
from time import sleep
from selenium.webdriver.support.select import Select
from case.public.export import export
from case.public.oprateTime import oprationTime
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class personalCardManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test189_personalCardManagement(self):
        u"""个人卡管理"""
        driver.find_element_by_link_text(u"卡管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"个人卡管理").click()
        sleep(2)

    def test190_cardType(self):
        u"""卡类型"""
        for i in range(1,3):
            s = driver.find_element_by_id("cardType")
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(2)
        s = driver.find_element_by_id("cardType")
        Select(s).select_by_index(0)
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)

    def test191_cardNumber(self):
        u"""卡号"""
        driver.find_element_by_id("cardCode").send_keys("200100012359")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)
        driver.find_element_by_link_text(u"详情").click()
        sleep(3)
        js = "document.getElementById('mainContent').scrollTop=10000"
        driver.execute_script(js)
        sleep(2)
        aet = export()
        aet.export()
        #消费记录
        driver.find_element_by_link_text(u"消费记录").click()
        sleep(6)
        js = "document.getElementById('mainContent').scrollTop=10000"
        driver.execute_script(js)
        sleep(2)
        driver.find_elements_by_class_name("textInput")[1].send_keys(u"何建欣")
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[2].send_keys(u"18645096021")
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[2].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[3].send_keys(u"1322111110000468")
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[3].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[4].send_keys(u"230104198907081233")
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[4].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        for i in range(1,4):
            s = driver.find_element_by_id("jiesuanType")
            Select(s).select_by_index(i)
            sleep(2)
            driver.find_elements_by_class_name("button")[4].click()
            sleep(5)

        s = driver.find_element_by_id("jiesuanType")
        Select(s).select_by_index(0)
        sleep(2)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        #开始时间
        #去掉readonly属性
        js = "document.getElementsByClassName('date')[0].removeAttribute('readonly');"
        driver.execute_script(js)
        #用js方法输入日期
        js_value = "document.getElementsByClassName('date')[0].value='2018-03-01'"
        driver.execute_script(js_value)
        #结束时间
        #去掉readonly属性
        js = "document.getElementsByClassName('date')[1].removeAttribute('readonly');"
        driver.execute_script(js)
        #用js方法输入日期
        js_value = "document.getElementsByClassName('date')[1].value='2018-07-24'"
        driver.execute_script(js_value)
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
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
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        det = export()
        det.export()
        epd = pageDisplay()
        epd.pageDisplay()
        fnd = numberDisplay()
        fnd.numberDisplay()

    def test192_oprateTime(self):
        u"""发卡时间"""
        driver.find_element_by_link_text(u"个人卡管理").click()
        sleep(3)
        op = oprationTime()
        op.oprationTime()

    def test193_cardState(self):
        u"""卡状态"""
        for i in range(1,5):
            s = driver.find_element_by_id("cardState")
            Select(s).select_by_index(i)
            sleep(2)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(3)
        s = driver.find_element_by_id("cardState")
        Select(s).select_by_index(0)
        sleep(2)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test194_cardHolder(self):
        u"""持卡人"""
        driver.find_elements_by_class_name("textInput")[3].send_keys(u"王帅")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_elements_by_class_name("textInput")[3].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test195_id(self):
        u"""身份证号"""
        driver.find_elements_by_class_name("textInput")[4].send_keys("410421198807062517")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test196_export(self):
        u"""导出"""
        ext = export()
        ext.export()
        driver.find_elements_by_class_name("textInput")[4].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test197_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test198_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()

if __name__ == '__main__':
    unittest.main()