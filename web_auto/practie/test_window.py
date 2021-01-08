# -*- coding:utf-8 -*-
from web_auto.practie.test_base import test_login
import time

class TestWindow(test_login):
    def test_windows(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@class="s-top-login-btn c-btn c-btn-primary c-btn-mini lb"]').click()
        self.driver.find_element_by_xpath('//*[@class="pass-reglink pass-link"]').click()
        print(self.driver.current_window_handle)  #打印当前窗口句柄
        print(self.driver.window_handles)   #打印所有窗口句柄
        windows = self.driver.window_handles  #参数化获取到的所有句柄
        self.driver.switch_to_window(windows[1])  #切换到需要跳转的窗口
        print(self.driver.current_window_handle)   #查看当前窗口是否已切换

        self.driver.find_element_by_xpath('//*[@name="userName"]').send_keys('nuannanxiaofeige')
        self.driver.switch_to_window(windows[0])   #切换回原窗口
        print(self.driver.current_window_handle)
        time.sleep(5)