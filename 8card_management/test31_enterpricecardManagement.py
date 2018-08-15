#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.export import export
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay
from selenium.webdriver.support.select import Select

driver = config.driver
class enterpriceCardManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test199_enterpriceCardManagement(self):
        u"""企业卡管理"""
        driver.find_element_by_link_text(u"卡管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"企业卡管理").click()
        sleep(3)

    def test200_enterpriceName(self):
        u"""企业名称"""
        driver.find_element_by_id("enterpriseName").send_keys(u"小易乐享租车")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(2)
        #详情
        driver.find_element_by_link_text(u"详情").click()
        sleep(5)
        aext = export()
        aext.export()
        js = "document.getElementsByClassName('tabsContent')[0].scrollTop = 10000"

        #末页
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
        cnd = numberDisplay()
        cnd.numberDisplay()
        #副卡信息
        driver.find_element_by_link_text(u"副卡信息").click()
        sleep(3)
        #按卡号查询
        driver.find_elements_by_class_name("textInput")[0].send_keys("200100011915")
        sleep(1)
        for i in range(2):
            driver.find_elements_by_class_name("button")[3].click()
            sleep(3)
        #按持卡人查询
        driver.find_elements_by_class_name("textInput")[1].send_keys("")
        driver.find_elements_by_class_name("button")[3].click()
        sleep(3)

        #按卡状态查询
        for i in range(1,5):
            s = driver.find_element_by_id("cardState")
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[3].click()
            sleep(3)
        s = driver.find_element_by_id("cardState")
        Select(s).select_by_index(0)
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(3)

        #检查翻页
        js = "document.getElementsByClassName('tabsContent')[0].scrollTop = 10000"
        #末页
        driver.execute_script(js)
        sleep(3)
        driver.find_element_by_link_text(u"末页").click()
        sleep(5)

        #首页
        driver.find_element_by_link_text(u"首页").click()
        sleep(5)
        js = "document.getElementsByClassName('tabsContent')[0].scrollTop = 10000"
        driver.execute_script(js)
        sleep(2)

        #设置每页显示条数
        dnm = numberDisplay()
        dnm.numberDisplay()

        #消费记录
        driver.find_element_by_link_text(u"消费记录").click()
        sleep(8)
        #按会员姓名进行查询
        driver.find_elements_by_class_name("textInput")[1].send_keys(u"")
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(5)

        #按电话进行查询
        driver.find_elements_by_class_name("textInput")[2].send_keys("18901330081")
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[2].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(5)

        #按机器编码进行查询
        driver.find_elements_by_class_name("textInput")[3].send_keys("0020150908001112")
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[3].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(5)

        #按证件号进行查询
        driver.find_elements_by_class_name("textInput")[4].send_keys("")
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[4].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(5)

        #按结算方式
        for i in range(1,4):
            s = driver.find_element_by_id("jiesuanType")
            Select(s).select_by_index(i)
            sleep(2)
            driver.find_elements_by_class_name("button")[3].click()
            sleep(5)

        s = driver.find_element_by_id("jiesuanType")
        Select(s).select_by_index(0)
        sleep(2)
        driver.find_elements_by_class_name("button")[3].click()
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
        driver.find_elements_by_class_name("button")[3].click()
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
        driver.find_elements_by_class_name("button")[3].click()
        sleep(5)

        #检查翻页
        epd = pageDisplay()
        epd.pageDisplay()

        #设置每页显示条数
        fnd = numberDisplay()
        fnd.numberDisplay()

    def test201_cardID(self):
        u"""卡号"""
        driver.find_element_by_link_text(u"企业卡管理").click()
        sleep(2)
        driver.find_element_by_id("cardCode").send_keys("200100010696")
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test202_export(self):
        u"""导出"""
        et = export()
        et.export()

    def test201_pageDisplay(self):
        u"""检查分页"""
        pd = pageDisplay()
        pd.pageDisplay()


    def test202_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()

    def test203_viceCard(self):
        u"""副卡"""
        driver.find_element_by_link_text(u"副卡").click()
        sleep(1)

    def test204_details(self):
        u"""详情"""
        driver.find_elements_by_link_text(u"详情")[3].click()
        sleep(8)
        #按会员姓名进行查询
        driver.find_elements_by_class_name("textInput")[1].send_keys(u"")
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)

        #按电话进行查询
        driver.find_elements_by_class_name("textInput")[2].send_keys("18610884088")
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[2].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)

        #按机器编码进行查询
        driver.find_elements_by_class_name("textInput")[3].send_keys("0102016021501260")
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[3].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)

        #按证件号进行查询
        driver.find_elements_by_class_name("textInput")[4].send_keys("")
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)
        driver.find_elements_by_class_name("textInput")[4].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[4].click()
        sleep(5)

        #按结算方式
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


    def test205_export(self):
        u"""导出副卡内容"""
        et = export()
        et.export()

    def test206_pageDilsplay(self):
        u"""检查翻页"""
        epd = pageDisplay()
        epd.pageDisplay()

    def test207_numberDisplay(self):
        u"""设置每页显示条数"""
        fnd = numberDisplay()
        fnd.numberDisplay()

if __name__ == '__main__':
    unittest.main()