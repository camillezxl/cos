#coding:utf-8
from config.config import config
from time import sleep

driver = config.driver
class pageDisplay():

    def pageDisplay(self):
        u"""翻页显示"""
        #滚动条回到底部
        js = "document.getElementsByClassName('layoutBox')[0].scrollTop = 10000"
        #翻页
        for i in range(1):
            driver.execute_script(js)
            sleep(2)
            driver.find_element_by_link_text(u"下一页").click()
            sleep(5)

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