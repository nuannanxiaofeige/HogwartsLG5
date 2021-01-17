# -*- coding:utf-8 -*-
from python_work.selenium_work2.page.base import Base
from python_work.selenium_work2.page.contact_page import ContactPage

_loc_addres=('xpath','//*[@id="menu_contacts"]')     #‘通讯录’

# 首页
class MainPage(Base):
    # 跳转通讯录页面
    def goto_contact_page(self):
        self.findElement(_loc_addres).click()
        return ContactPage(self.driver)
