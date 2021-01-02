import pytest

# def add_fun(a,b):
#     return  a+b
#
# @pytest.mark.parametrize("a,b,expected",[(1,2,3),(2,2,4)],ids=["int","float"])
# def test_add(a,b,expected):
#     assert add_fun(a,b)==expected

# 参数可以使用堆叠使用
@pytest.mark.parametrize('a',[1,3,5])
@pytest.mark.parametrize("b",[2,4,6])
def test_add(a,b):
    print("测试参数堆叠的组合：a->%s，b->%s"%(a,b))