#coding:utf-8
from config.config import config
from time import sleep

driver = config.driver
class numberDisplay():

    def numberDisplay(self):
        u"""每页显示条数"""
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(2)
        index = [20,50,100]
        for i in index:
            driver.find_element_by_link_text(i).click()
            sleep(2)
            js = "document.getElementsByClassName('tableList')[0].scrollTop = 10000"
            driver.execute_script(js)
            sleep(3)
            s = driver.find_element_by_link_text(i)
            s.click()
            sleep(3)
        s = driver.find_element_by_link_text(10)
        s.click()
        sleep(3)

