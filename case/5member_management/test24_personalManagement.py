#coding:utf-8
import unittest
from config.config import config
from time import sleep
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class personalManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test156_personalManagement(self):
        u"""个人会员管理"""
        driver.find_element_by_link_text(u"会员管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"个人会员管理").click()
        sleep(3)

    def test157_memberName(self):
        u"""会员姓名"""
        driver.find_element_by_id("memberName").send_keys("13929568903")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)
        #查看详情
        driver.find_element_by_link_text(u"详情").click()
        sleep(5)
        driver.find_element_by_link_text(u"个人会员管理").click()
        sleep(3)

    def test158_id(self):
        u"""身份证号"""
        driver.find_elements_by_class_name("textInput")[1].send_keys("522101198201082068")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test159_phone(self):
        u"""电话号码"""
        driver.find_elements_by_class_name("textInput")[2].send_keys("13810189250")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)

    def test160_oprateTime(self):
        u"""开户时间"""
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

    def test161_pageDisplay(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test162_numberDisplay(self):
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