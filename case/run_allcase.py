#coding:utf-8
import HTMLTestRunnerCN
import time,unittest
import SendEmail

listaa = r"E:\\Python\\cos\\case\\"

report_dir = r"E:\\\Python\\cos\\report\\"
def createSuite1():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa,pattern='test*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            print 'adding test...' + str(test_case)
            testunit.addTests(test_case)
    return testunit

today = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime())
test_report = report_dir
filename = test_report + today + 'result.html'

fp = open(filename,'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title=u'富电充电运营管理平台测试报告',description=u'富电充电运营管理后台自动化测试报告')
runner.run(createSuite1())
fp.close()

new_report = SendEmail.new_report(test_report)
SendEmail.send_file(new_report)     #发送测试报告