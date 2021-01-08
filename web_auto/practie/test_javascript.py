# -*- coding:utf-8 -*-
from web_auto.practie.test_base import test_login
import time
import pytest

class TestJs(test_login):
    @pytest.mark.skip()
    def test_js(self):
        self.driver.get("http://www.baidu.com")
        self.driver.execute_script("return document.getElementById=kw").send_keys("selenium")
        self.driver.execute_script("return document.getElementById=su").click()
        self.driver.execute_script("return document.documentElement.scrollTop=10000")  #滑动到页面底部
        time.sleep(3)
        '''打印title和页面性能信息'''
        print(self.driver.execute_script("return document.title;return JSON.stringfy(performance.timing)"))


    def test_datatime(self):
        self.driver.get("https://www.12306.cn/index/")
        time.sleep(2)
        times=self.driver.execute_script("return document.getElementById=('train_date')") #定位元素
        # time.sleep(2)
        # times.removeAttribute('readonly')  #需要查看页面元素是否有readonly属性
        time.sleep(2)
        self.driver.execute_script("document.getElementById=('train_date').value='2021-02-06'")#修改时间
