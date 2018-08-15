#coding:utf-8
import unittest
from config.config import config
from time import sleep

driver = config.driver
class privateManagement(unittest.TestCase):
    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test175_privateManagement(self):
        u"""私桩管理"""
        driver.find_element_by_link_text(u"私桩管理").click()
        sleep(1)
        driver.find_elements_by_link_text(u"私桩管理")[1].click()
        sleep(2)

    def test176_pileCode(self):
        u"""充电桩编号"""

    def test177_phone(self):
        u"""主用户手机"""

    def test178_machineState(self):
        u"""设备状态"""

    def test179_area(self):
        u"""所属地区"""

    def test180_add(self):
        u"""添加"""
        driver.find_element_by_link_text(u"添加").click()
        sleep(2)
        driver.find_elements_by_class_name("button")[3].click()
        sleep(2)

    def test181_numberDisplay(self):
        u"""设置每页显示条数"""


if __name__ == '__main__':
    unittest.main()