#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.receiveState import receiveState
import SendKeys
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay
from case.public.export import export

driver = config.driver
class anonymouseCardBatchManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test227_anonymouseCardBatchManagement(self):
        u"""不记名卡批次管理"""
        driver.find_element_by_link_text(u"卡管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"不记名卡批次管理").click()
        sleep(3)

    def test228_batchName(self):
        u"""批次名称"""
        driver.find_elements_by_class_name("textInput")[0].send_keys(u"富电新能源12-4")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        driver.find_element_by_link_text(u"详情").click()
        sleep(3)
        driver.find_elements_by_class_name("textInput")[0].send_keys("18511519675")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        driver.find_elements_by_class_name("textInput")[0].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        ars = receiveState()
        ars.receiveState()
        driver.find_element_by_link_text(u"导出").click()
        sleep(6)
        SendKeys.SendKeys("{ENTER}")
        sleep(3)
        driver.find_element_by_link_text(u"导出兑换码").click()
        sleep(6)
        SendKeys.SendKeys("{ENTER}")
        sleep(3)
        bpd = pageDisplay()
        bpd.pageDisplay()

        cnd = numberDisplay()
        cnd.numberDisplay()

        #消费记录
        driver.find_element_by_link_text(u"消费记录").click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[0].send_keys("AA9000000068")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        driver.find_elements_by_class_name("textInput")[0].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)

        driver.find_elements_by_class_name("textInput")[1].send_keys("0102016021501261")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)

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
        driver.find_elements_by_class_name("button")[0].click()
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
        driver.find_elements_by_class_name("button")[0].click()
        sleep(5)
        driver.find_element_by_partial_link_text(u"导出").click()
        sleep(6)
        driver.find_element_by_xpath(".//*[@id='images']/li/a/img").click()
        sleep(2)
        SendKeys.SendKeys("{ENTER}")
        sleep(3)
        #末页
        js = "document.getElementsByClassName('pageFormContent')[0].scrollTop = 10000"
        driver.execute_script(js)
        sleep(3)
        driver.find_element_by_link_text(u"末页").click()
        sleep(5)

        #首页
        driver.execute_script(js)
        sleep(3)
        driver.find_element_by_link_text(u"首页").click()
        sleep(5)
        driver.execute_script(js)
        sleep(2)

        end = numberDisplay()
        end.numberDisplay()

    def test229_oprateName(self):
        u"""创建时间"""
        driver.find_element_by_link_text(u"不记名卡批次管理").click()
        sleep(2)
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
        driver.find_elements_by_class_name("button")[0].click()
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
        driver.find_elements_by_class_name("button")[0].click()
        sleep(5)


    def test230_addBatch(self):
        u"""添加批次"""
        driver.find_element_by_link_text(u"添加批次").click()
        sleep(3)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)

    def test231_export(self):
        u"""导出"""
        ex = export()
        ex.export()

    def test232_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()



if __name__ == '__main__':
    unittest.main()