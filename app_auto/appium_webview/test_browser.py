# -*- coding:utf-8 -*-

from appium import webdriver
from time import sleep

class TestBrowser():
    def setup(self):
        des_caps={
            "platformName":"android",
            "platformVersion":"6.0",
            "browserName":"Browser",
            "noReset":True,
            "deviceName":"127.0.0.1:7555",
            'chromedriverExecutable':'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Appium\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\\win\\chromedriver.exe',
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)