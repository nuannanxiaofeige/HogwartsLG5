# -*- coding:utf-8 -*-
from python_work.appium_work3.app import App


class TestCase():
    def test_black(self):
        app=App()
        app.start().go_main().goto_market()
