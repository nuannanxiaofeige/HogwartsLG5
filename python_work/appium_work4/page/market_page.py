# -*- coding:utf-8 -*-


from python_work.appium_work4.base_page import BasePage



class MarketPage(BasePage):
    def goto_search(self):
        self.run_steps("../page/market_page.yaml","goto_search")
        return True

