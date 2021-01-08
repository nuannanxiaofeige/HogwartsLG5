# -*- coding:utf-8 -*-


from selenium import webdriver
from time import sleep
import json


class TestWx():
    # 浏览器复用：本地打开一个浏览器
    def setup_method(self):
        Chrome_args= webdriver.ChromeOptions()
        Chrome_args.debugger_address="localhost:9222"
        self.driver=webdriver.Chrome(options=Chrome_args)

    def test_click(self):
        # 获取当前cookie
        cookies=self.driver.get_cookies()
        # 将cookie写入cookie.json中
        with open("cookie.json","w") as f:
            cookies=json.dumps(cookies,f)

        # 打开浏览器，注入cookie
        self.driver.get("")
        # 将cookie读取出来
        with open("cookie.json","r") as f:
            cookies=json.load(f)
            print(cookies)

        for cookie in cookies:
            # 将cookie以字典的形势添加到selenium
            self.driver.add_cookie(cookie)
        # 添加完成在访问已经登录的页面
        self.driver.get('')



