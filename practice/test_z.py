import pytest
import yaml

def fun(a,b):
    return a+b

@pytest.mark.parametrize("a,b,expected",yaml.safe_load(open("../config/z.yml"))["datas"],
                                                       ids=yaml.safe_load(open("../config/z.yml"))["myids"])
def test_z(a,b,expected):
    assert fun(a,b)==expected