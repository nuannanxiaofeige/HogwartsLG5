# -*- coding:utf-8 -*-
import json

import pytest

from python_work.selenium_work2.page.main_page import MainPage
from selenium import webdriver

success_name='行政部门'
fail_name='行政部门'

class Test_AddDepartment():
    def setup_method(self):
        self.main=MainPage()  #获取cookie前需要注掉
        # chrome_ages = webdriver.ChromeOptions()
        # chrome_ages.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=chrome_ages)
        # with open('cookie.json','w',encoding='utf-8') as f:
        #     json.dump(self.driver.get_cookies(),f)

    def teardown_method(self):
        # self.main.driver.quit()
        pass
    def test_add_department_success(self):
        res=self.main.goto_contact_page().add_department_success(success_name).get_list()
        assert success_name in res
    #
    def test_add_department_fail(self):
        res=self.main.goto_contact_page().add_department_fail(fail_name).get_list()
        assert res.count(fail_name) == 1

if __name__ =='__main__':
    pytest.main(['test_add_department.py','-sq'])