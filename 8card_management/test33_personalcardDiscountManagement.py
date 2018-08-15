#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.export import export
from case.public.numberDisplay import numberDisplay

driver = config.driver
class personalCardDiscountManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test214_personalCardDiscountManagement(self):
        u"""个人卡优惠管理"""
        driver.find_element_by_link_text(u"卡管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"个人卡优惠管理").click()
        sleep(2)

    def test215_discountName(self):
        u"""优惠名称"""
        driver.find_elements_by_class_name("textInput")[0].send_keys(u"充值1600-8折")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)
        driver.find_element_by_link_text(u"详情").click()
        sleep(2)
        driver.find_element_by_id("cardCode").send_keys("200100006499")
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(2)
        driver.find_element_by_id("cardCode").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(2)
        driver.find_elements_by_class_name("textInput")[1].send_keys("132924197605262250")
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(2)
        driver.find_elements_by_class_name("textInput")[1].clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(2)
        #检查翻页
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

        #设置每页显示条数
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(2)
        index = [20,50,100]
        for i in index:
            driver.find_element_by_link_text(i).click()
            sleep(2)
            js = "document.getElementsByClassName('pageFormContent')[0].scrollTop = 10000"
            driver.execute_script(js)
            sleep(3)
            s = driver.find_element_by_link_text(i)
            s.click()
            sleep(3)
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(3)

        driver.find_elements_by_link_text(u"详情")[2].click()
        sleep(3)

        js = "document.getElementById('mainContent').scrollTop=10000"
        driver.execute_script(js)
        aet = export()
        aet.export()

        #设置每页显示条数
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(2)
        index = [20,50,100]
        for i in index:
            driver.find_element_by_link_text(i).click()
            sleep(2)
            js = "document.getElementById('mainContent').scrollTop = 10000"
            driver.execute_script(js)
            sleep(3)
            s = driver.find_element_by_link_text(i)
            s.click()
            sleep(3)
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(3)

        driver.find_element_by_link_text(u"消费记录").click()
        sleep(5)
        bet = export()
        bet.export()
        #检查翻页
        #末页
        js = "document.getElementById('mainContent').scrollTop = 10000"
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

        #设置每页显示条数
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(2)
        index = [20,50,100]
        for i in index:
            driver.find_element_by_link_text(i).click()
            sleep(2)
            js = "document.getElementById('mainContent').scrollTop = 10000"
            driver.execute_script(js)
            sleep(3)
            s = driver.find_element_by_link_text(i)
            s.click()
            sleep(3)
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(3)

    def test216_oprateTime(self):
        u"""创建时间"""
        driver.find_element_by_link_text(u"个人卡优惠管理").click()
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

    def test217_addDiscount(self):
        u"""添加优惠"""
        driver.find_element_by_link_text(u"添加优惠").click()
        sleep(2)
        driver.find_element_by_link_text(u"返回").click()
        sleep(2)

    def test218_numberDisplay(self):
        u"""设置每页显示条数"""
        nd = numberDisplay()
        nd.numberDisplay()

if __name__ == '__main__':
    unittest.main()