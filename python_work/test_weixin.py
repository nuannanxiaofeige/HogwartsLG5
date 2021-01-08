# -*- coding:utf-8 -*-


from selenium import webdriver
import json
from time import sleep



'''
作业:
使用 cookie 和浏览器复用，实现企业微信的点击客户联系
'''

class TestWx():
    def setup_method(self):
        chrome_ages=webdriver.ChromeOptions()
        chrome_ages.debugger_address='localhost:9222'
        self.driver=webdriver.Chrome()

    # def teardown_method(self):
    #     pass

    def test_getcookie(self):
        # cookies=self.driver.get_cookies()
        # with open("cookie.json","w")as f:
        #     json.dump(cookies,f)

        self.driver.get("https://work.weixin.qq.com")
        with open("cookie.json","r") as f:
            cookies=json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_xpath("//*[@class='frame_head_bottom_stage']//a[4]").click()
