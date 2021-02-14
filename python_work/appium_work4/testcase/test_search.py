# -*- coding:utf-8 -*-
import pytest
import yaml

from python_work.appium_work4.app import App

# def get_data():
#     with open ("../data/data.yaml","r",encoding="utf-8") as f:
#         data = yaml.safe_load(f)
#         add_data= data["add"]
#         return add_data

class  TestSearch():
    # @pytest.mark.parametrize("text")
    def test_search(self):
        app = App()
        res = app.start().goto_main().goto_market().goto_search()
        assert res

    def test_mine(self):
        app=App()
        app.start().goto_main().goto_mine()
