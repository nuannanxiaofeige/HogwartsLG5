# -*- coding:utf-8 -*-


# 初始化driver
import yaml
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as by






class BasePage:

    def __init__(self,driver=None):    #第一次是没有driver信息，给个默认值None
        self.driver = driver

    def findElement(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","valuel")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver,timeout=15).until(lambda x: x.find_element(*locator))
            return ele

    def sendKeys(self,locator,text):
        a = self.findElement(locator)
        a.send_keys(text)

    def click(self,locator):
        a = self.findElement(locator)
        a.click()

    def get_text(self,locator):
        '''获取文本'''
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取文本失败，返回' '")
            return " "

    # 滑动查找点击
    def scoller_click(self,text):
        self.driver.find_element(by.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector().'
                             'scrollable(true).instance(0)).'
                             'scrollIntoView(new UiSelector().'
                             f'text("{text}").instance(0));').click()

