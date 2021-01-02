# coding:utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest,time


class Testcase():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_click(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
        dan = self.driver.find_element_by_css_selector('#su')
        action=ActionChains(self.driver)
        action.click(dan)  #点击定位到的元素
        action.perform()

    # 将鼠标移动至设置，然后点击搜索设置
    def test_move_mouse(self):
        self.driver.get("http://www.baidu.com")
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')).perform()
        ActionChains(self.driver).click(self.driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]')).perform()


if __name__=="__main__":
    pytest.main(Testcase)