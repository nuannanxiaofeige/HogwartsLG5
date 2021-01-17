from selenium import webdriver

class TestClick():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_baidu(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
        self.driver.find_element_by_css_selector('#su').click()
        self.driver.save_screenshot("./result/1.png")


 