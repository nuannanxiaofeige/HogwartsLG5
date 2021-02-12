# -*- coding:utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy as by

from python_work.appium_work3.base_page import BasePage

loc_market=(by.XPATH,"//*[@text='行情']")

class MainPage(BasePage):
    def goto_market(self):
        self.click(loc_market)
        return True

