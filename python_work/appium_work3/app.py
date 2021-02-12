# -*- coding:utf-8 -*-

#启动app，关闭app，重启app，进入首页。。。
from appium import webdriver

from python_work.appium_work3.base_page import BasePage
from python_work.appium_work3.page.main_page import MainPage
from appium.webdriver.common.mobileby import MobileBy as by

loc_redact=(by.XPATH,"//*[@resource-id='com.xueqiu.android:id/post_status']")

class  App(BasePage):
    def start(self):
        # 第一次开始的时候driver为空，创建一个driver
        if self.driver == None:
            desired_caps = {}
            desired_caps["platformName"] = "android"
            desired_caps["platformVersion"] = '6.0'
            desired_caps["deviceName"] = "127.0.0.1:7555"
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = '.common.MainActivity'  # 从当前页面开始点击
            # 不清空本地缓存，启动app
            desired_caps["noReset"] = "true"
            # desired_caps["dontStopAppOnReset"]='true',  # 不退出应用
            desired_caps["skipDeviceInitialization"] = 'true'  # 跳过一些安装、权限的步骤，提升运行速度
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()    #自动把capabilities里的一些参数传入
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return  self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self)->MainPage:
        return MainPage(self.driver)


    # 制造一个弹窗
    def go_main(self):
        self.click(loc_redact)
        return MainPage(self.driver)