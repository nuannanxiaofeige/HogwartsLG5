# -*- coding:utf-8 -*-
from appium import webdriver
import pytest
import time

class Test_AddContact():

    def setup(self):
        desired_caps = {}
        desired_caps["platformName"] = "android"
        desired_caps["platformVersion"] = '6.0'
        desired_caps["deviceName"] = "127.0.0.1:7555"
        desired_caps["appPackage"] = "com.tencent.wework"
        desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
        desired_caps["noReset"] = "true"
        # desired_caps["dontStopAppOnReset"]='true',  # 不退出应用
        desired_caps["skipDeviceInitialization"] = 'true'  # 跳过一些安装、权限的步骤，提升运行速度
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_contact(self):
        self.driver.find_element_by_xpath("//.[@resource-id='com.tencent.wework:id/elq'and @text='通讯录']").click()
        self.driver.find_element_by_xpath("//.[@class='android.widget.TextView' and @text='添加成员']").click()
        self.driver.find_element_by_xpath("//.[@class='android.widget.TextView' and @text='手动输入添加']").click()
        self.driver.find_element_by_xpath \
            (
                "//android.widget.ScrollView[@resource-id='com.tencent.wework:id/bck']//android.widget.RelativeLayout[@resource-id='com.tencent.wework:id/ern']//android.widget.EditText[@resource-id='com.tencent.wework:id/b78']").send_keys(
            "王大")
        self.driver.find_element_by_xpath("//.[@class='android.widget.EditText'and @text='手机号']").send_keys(
            "12345678910")
        self.driver.find_element_by_xpath("//.[@class='android.widget.TextView'and @text='设置部门']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/gzz").click()
        self.driver.find_element_by_id("com.tencent.wework:id/ie7").click()
        time.sleep(5)
        self.driver.find_element_by_id("com.tencent.wework:id/idp").click()


if __name__ == "__main__":
    pytest.main()
