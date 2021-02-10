# -*- coding:utf-8 -*-


# 填写成员信息
import pytest
from appium.webdriver.common.mobileby import MobileBy as by

from python_work.appium_work2.page.basepage import BasePage



loc_name = (by.XPATH, "//android.widget.ScrollView[@resource-id='com.tencent.wework:id/bck']"
                            "//android.widget.RelativeLayout[@resource-id='com.tencent.wework:id/ern']//a" 
                          "ndroid.widget.EditText[@resource-id='com.tencent.wework:id/b78']")
loc_genderman = (by.XPATH, "//.[@text='男']")
loc_genderwoman = (by.XPATH, "//.[@text='女']")
loc_phone =(by.XPATH, "//.[@class='android.widget.EditText'and @text='手机号']")
loc_setting =(by.XPATH, "//.[@class='android.widget.TextView'and @text='设置部门']")
loc_confirm =(by.XPATH, "//.[@resource-id='com.tencent.wework:id/gzz']")
loc_save = (by.XPATH,"//.[@resource-id='com.tencent.wework:id/ie7']")



class ConactEditPage(BasePage):

    def add_membership_information(self,name,gender,phone):
        self.sendKeys(loc_name,name)
        self.click(loc_genderman)
        if gender == '女':
            self.click(loc_genderwoman)
        else:
            self.click(loc_genderman)

        self.sendKeys(loc_phone,phone)
        self.click(loc_setting)
        self.click(loc_confirm)

        self.click(loc_save)
        from python_work.appium_work2.page.memberinvite_page import MemberInvitePage
        return MemberInvitePage(self.driver)
