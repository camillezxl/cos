#coding:utf-8
from config.config import config
from time import sleep
from selenium.webdriver.support.select import Select

driver = config.driver
class receiveState():
    def receiveState(self):
        u"""领取状态"""
        for i in range(2):
            s = driver.find_element_by_id("receiveStatus")
            Select(s).select_by_index(i)
            sleep(1)
            driver.find_elements_by_class_name("button")[0].click()
            sleep(2)
        s = driver.find_element_by_id("receiveStatus")
        Select(s).select_by_index(0)
        sleep(1)
        driver.find_elements_by_class_name("button")[0].click()
        sleep(2)