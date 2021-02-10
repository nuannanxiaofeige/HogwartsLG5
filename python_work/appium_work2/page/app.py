# -*- coding:utf-8 -*-

#启动app，关闭app，重启app，进入首页。。。
from appium import webdriver

from python_work.appium_work2.page.basepage import BasePage
from python_work.appium_work2.page.main_page import MainPage


class  App(BasePage):
    def start(self):
        # 第一次开始的时候driver为空，创建一个driver
        if self.driver == None:
            desired_caps = {}
            desired_caps["platformName"] = "android"
            desired_caps["platformVersion"] = '6.0'
            desired_caps["deviceName"] = "127.0.0.1:7555"
            desired_caps["appPackage"] = "com.tencent.wework"
            desired_caps["appActivity"] = ".launch.LaunchSplashActivity"
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
