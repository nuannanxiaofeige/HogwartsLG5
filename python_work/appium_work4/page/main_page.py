# -*- coding:utf-8 -*-
from python_work.appium_work4.base_page import BasePage
from python_work.appium_work4.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.run_steps("../page/main_page.yaml","goto_market")

        return MarketPage(self.driver)

    def goto_mine(self):
        self.run_steps("../page/main_page.yaml","goto_mine")
        return True