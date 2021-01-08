# -*- coding:utf-8 -*-
from selenium  import webdriver

class test_login():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        # self.driver.quit()
        pass