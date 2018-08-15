#coding:utf-8
import unittest
from config.config import config
from time import sleep

driver = config.driver
class connectJournal(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        sleep(1)

    def test140_connectJournal(self):
        u"""连接日志"""
        driver.find_element_by_link_text(u"设备管理").click()
        sleep(1)
        driver.find_element_by_link_text(u"连接日志").click()
        sleep(5)

    def test141_pileCode(self):
        u"""充电桩机器编号"""


    def test142_city(self):
        u"""站点城市"""

    def test143_oprate(self):
        u"""操作时间"""


    def test144_numDisplay(self):
        u"""每页显示条数"""


if __name__ == '__main__':
    unittest.main()