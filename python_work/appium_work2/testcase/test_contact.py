# -*- coding:utf-8 -*-
import pytest
import yaml

from python_work.appium_work2.page.app import App

def get_data():
    with open ('../data/data.yml',encoding="utf-8") as f:
        data = yaml.safe_load(f)
        add_data = data["add"]
        return  add_data

class TestContact():
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()


    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phone",get_data())
    def test_add_contact(self,name,gender,phone):
        toast=self.main.click_addresslist().add_member().addconect_menual().add_membership_information(name,gender,phone).get_toast()
        assert toast=='添加成功'

# if __name__=="__main__":
#     # print(get_data())