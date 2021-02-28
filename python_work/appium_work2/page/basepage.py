# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-


# 初始化driver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy as by
from selenium.webdriver.support import expected_conditions as EC
from python_work.appium_work3.page.black_handle import black_handle





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
        a = self.findElementNew(locator)
        a.send_keys(text)

    def click(self,locator):
        a = self.findElementNew(locator)
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


    '''定位到元素返回元素对象，未定位到返回TimeOut异常,并且对黑名单进行操作（点击【X】） '''
    @black_handle
    def findElementNew(self,locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","valuel")')
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" % (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, timeout=15,).until(EC.presence_of_element_located(locator))
            return ele

