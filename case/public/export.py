#coding:utf-8
from config.config import config
from time import sleep

driver = config.driver
class export():

    def export(self):
        u"""导出"""
        driver.find_element_by_partial_link_text(u"导出").click()
        sleep(6)