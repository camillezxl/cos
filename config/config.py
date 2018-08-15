#coding:utf-8
from selenium import webdriver
from time import sleep

class config():
    u"""启动浏览器"""
    #配置文件地址
    profile_directory = r"C:\Users\Allen\AppData\Roaming\Mozilla\Firefox\Profiles\3x6dxhmg.default"
    #加载配置文件
    profile = webdriver.FirefoxProfile(profile_directory)
    #设置成0表示下载到桌面；设置成1表示下载到默认路径；设置成2表示下载到指定路径
    profile.set_preference('browser.download.folderList',2)
    #制定文件到你想存放的路径
    profile.set_preference('browser.download.dir',r'E:\\Python\\cos\\download\\')
    #开始下载时是否显示进度条
    profile.set_preference('browser.download.manager.showWhenStarting',False)
    #对所给出的文件类型不再弹出框询问
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/octet-stream ,application/zip,application/kswps,application/vnd.ms-excel,application/x-xls')
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get(r"http://cos.telluspowertech.cn/auth/home.action#")
    sleep(5)
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_id("user").send_keys("zybjjg")
    driver.find_element_by_id("pass").send_keys("zy5269")
    driver.find_element_by_id("login").click()
    sleep(3)