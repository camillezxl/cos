#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class personalCardGroupManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test208_personalCardGroupManagement(self):
        u"""个人卡组管理"""
        driver.find_element_by_link_text(u"卡管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"个人卡组管理").click()
        sleep(3)

    def test209_cardGroupName(self):
        u"""卡组名称"""
        driver.find_elements_by_class_name("textInput")[0].send_keys(u"华贸物业")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)
        driver.find_elements_by_link_text(u"详情")[1].click()
        sleep(3)

    def test210_oprateTime(self):
        u"""创建时间"""
        driver.find_element_by_link_text(u"个人卡组管理").click()
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


    def test211_addCardGroup(self):
        u"""添加卡组"""
        driver.find_element_by_link_text(u"添加卡组").click()
        sleep(2)
        driver.find_element_by_link_text(u"返回").click()
        sleep(2)


    def test212_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test213_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()


if __name__ == '__main__':
    unittest.main()