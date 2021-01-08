# -*- coding:utf-8 -*-

from web_auto.practie.test_base import test_login
from selenium.webdriver import ActionChains
from time import  sleep


class TestAlert(test_login):

    def test_alert(self):
        self.driver.get("http://www.baidu.com")
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')).perform()
        ActionChains(self.driver).click(self.driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div[1]/a[1]')).perform()
        self.driver.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()
        self.driver.switch_to.alert.accept()
        sleep(2)