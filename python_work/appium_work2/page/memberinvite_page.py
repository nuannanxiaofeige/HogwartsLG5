# -*- coding:utf-8 -*-

# 点击手动添加
from appium.webdriver.common.mobileby import MobileBy as by

from python_work.appium_work2.page.basepage import BasePage
from python_work.appium_work2.page.conactedit_page import ConactEditPage

loc1 = (by.XPATH,"//.[@class='android.widget.TextView' and @text='手动输入添加']")
loc2 = (by.XPATH,"//.[@class='android.widget.Toast']")

class MemberInvitePage(BasePage):

    def addconect_menual(self):
        self.click(loc1)
        return ConactEditPage(self.driver)

    def get_toast(self):
        ele = self.get_text(loc2)
        return ele



