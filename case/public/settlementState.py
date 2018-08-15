#coding:utf-8
from config.config import config
from time import sleep
from selenium.webdriver.support.select import Select

driver = config.driver
class settlementState():

    def settlementState(self):
        u"""结算状态"""
        for i in range(1,7):
            s = driver.find_element_by_id("settlementStatus")
            Select(s).select_by_index(i)
            sleep(2)
            driver.find_elements_by_class_name("button")[1].click()
            sleep(5)

        s = driver.find_element_by_id("settlementStatus")
        Select(s).select_by_value("")
        sleep(2)
        driver.find_elements_by_class_name("button")[1].click()
        sleep(5)