# -*- coding:utf-8 -*-

import pytest
import yaml
import allure
from python_work.calculate import Calculate

'''
课后作业
补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
将 fixture 方法存放在 conftest.py ，设置 scope=module
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合 allure 生成本地测试报告
'''
@allure.feature('加减乘除运算模块')
class  TestCalculate():
# 加法
    @allure.story('加法运算')
    @pytest.mark.run(order=1)
    def test_add(self,get_cala,get_add):
        res=None
        try:
            res=get_cala.add(get_add[0],get_add[1])
        except Exception as e:
            print(f'异常信息：{e}')
        print(res)
        assert res==get_add[2]

# 除法
    @allure.story('除法运算')
    @pytest.mark.run(order=4)
    def test_div(self,get_cala,get_div):
        res=None
        try:
            res = get_cala.div(get_div[0], get_div[1])
            if isinstance(res,float):
                res=round(res,2)
        except Exception as e:
            print(f"异常信息：{e}")
        print(res)
        assert res==get_div[2]

# 减法
    @allure.story('减法运算')
    @pytest.mark.run(order=2)
    def test_sub(self,get_cala,get_sub):
        res=None
        try:
             res=get_cala.sub(get_sub[0],get_sub[1])
        except Exception as e:
            print(f"异常信息：{e}")
        print(res)
        assert res==get_sub[2]

# 乘法
    @allure.story('乘法运算')
    @pytest.mark.run(order=3)
    def test_mul(self,get_cala,get_mul):
        res=None
        try:
            res=get_cala.mul(get_mul[0],get_mul[1])
        except Exception as e:
            print(f"异常信息：{e}")
        print(res)
        assert res==get_mul[2]
