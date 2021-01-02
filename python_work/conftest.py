import pytest
from python_work.calculate import Calculate
import yaml


@pytest.fixture(scope='module')
def get_cala():
    print('-----开始计算-----')
    cala=Calculate()
    yield cala
    print('-----计算结束-----')

with open('../config/calculate.yml') as f:
    datas=yaml.safe_load(f)
    add_data=datas['add']
    sub_data=datas['subtract']
    mul_data=datas['multiply']
    div_data=datas['division']
    myids=datas['myids']

#加法
@pytest.fixture(params=add_data,ids=myids)
def get_add(request):
    add= request.param
    print("\n开始加法计算")
    return add

# 减法
@pytest.fixture(params=sub_data,ids=myids)
def get_sub(request):
    sub= request.param
    print("\n开始减法计算")
    return sub

# 乘法
@pytest.fixture(params=mul_data,ids=myids)
def get_mul(request):
    mul=request.param
    print("\n开始乘法计算")
    return mul

# 除法
@pytest.fixture(params=div_data,ids=myids)
def get_div(request):
    div=request.param
    print("\n开始除法计算")
    return div


