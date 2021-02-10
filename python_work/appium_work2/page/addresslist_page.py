# -*- coding:utf-8 -*-

# 点击添加成员
from appium.webdriver.common.mobileby import MobileBy as by


from python_work.appium_work2.page.basepage import BasePage
from python_work.appium_work2.page.memberinvite_page import MemberInvitePage

# loc_address = (by.XPATH,"//.[@class='android.widget.TextView' and @text='添加成员']")
text  = '添加成员'

class AddressListPage(BasePage):
    def add_member(self):
        self.scoller_click(text)
        # self.driver.find_element(by.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        # self.driver.findElement(loc_address).click()
        return MemberInvitePage(self.driver)