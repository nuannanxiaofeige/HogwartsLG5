# coding:utf-8


from selenium import webdriver
from selenium.webdriver import TouchActions
import time

class Test_TouchActions():

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()



    def test_touchactions(self):
        '''
            在搜索框中输入“selenium测试 ”
            通过touchAction点击搜索框
            滑动到底部，点击下一页
            关闭chrome
        '''
        inp=self.driver.find_element_by_xpath('//*[@id="kw"]')
        search=self.driver.find_element_by_xpath('//*[@id="su"]')
        action=TouchActions(self.driver)
        inp.send_keys("selenium测试")
        action.tap(search).perform()
        action.scroll_from_element(search,0,10000).perform()
        next_page=self.driver.find_element_by_xpath('//*[@class="page-inner"]/a[10]')
        action.tap(next_page).perform()

