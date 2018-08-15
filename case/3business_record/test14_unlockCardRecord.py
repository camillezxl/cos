#coding:utf-8
import unittest
from time import sleep
from config.config import config
from case.public.export import export
from case.public.pageDisplay import pageDisplay
from case.public.numberDisplay import numberDisplay

driver = config.driver
class unlockCardRecord(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test091_unlockCardRecord(self):
        u"""解锁卡记录"""
        driver.find_element_by_link_text(u"业务记录").click()
        sleep(1)
        driver.find_element_by_link_text(u"解锁卡记录").click()
        sleep(3)

    def test092_cardNumber(self):
        """按解锁卡号查询"""
        driver.find_element_by_id("cardNumber").send_keys("200100007114")
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)
        driver.find_element_by_id("cardNumber").clear()
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(3)


    def test093_oprateTime(self):
        u"""按解锁时间查询"""
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

    def test094_export(self):
        u"""导出"""
        et = export()
        et.export()

    def test095_pageDispage(self):
        u"""检查翻页"""
        pd = pageDisplay()
        pd.pageDisplay()

    def test096_numberDispage(self):
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