# -*- coding:utf-8 -*-

# 点击通讯录
from appium.webdriver.common.mobileby import MobileBy as by

from python_work.appium_work2.page.addresslist_page import AddressListPage
from python_work.appium_work2.page.basepage import BasePage

loc_concat = (by.XPATH,"//.[@resource-id='com.tencent.wework:id/elq'and @text='通讯录']")


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    def click_addresslist(self):
        self.click(loc_concat)
        return AddressListPage(self.driver)


