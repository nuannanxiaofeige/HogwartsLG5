# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
import json



class Base():
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self.driver=webdriver.Chrome()
            self._getcookie()
        else:
            self.driver=driver
            self.driver.maximize_window()


    # 获取cookie
    def write_cookie(self):
        self.driver.get("https://work.weixin.qq.com")
        cookies=self.driver.get_cookies()
        with open("cookie.json","w")as f:
            json.dump(cookies,f)
    #
    def _getcookie(self):
        self.driver.get("https://work.weixin.qq.com")
        with open("cookie.json", "r") as f:
            cookies=json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def findElement(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","valuel")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver,timeout=15).until(lambda x: x.find_element(*locator))
            return ele

    def sendKeys(self, locator, text):
        a = self.findElement(locator)
        a.send_keys(text)
