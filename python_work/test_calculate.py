# 参数调用
import pytest
import yaml
from python_work.calculate import Calculate

# 把获取yml文件封装成一个函数,方便调用
def get_calculate():
    with open("../config/calculate.yml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add"]
        subtract_datas=datas["subtract"]
        multiply_datas =datas["multiply"]
        division_datas=datas["division"]
        add_ids = datas["myids"]
        return [add_datas, subtract_datas,multiply_datas, division_datas,add_ids]

class Test_Calculate():

    def setup_class(self):
        self.cal = Calculate()
        print("计算加减乘除")

    def teardown_class(self):
        print("所有计算已结束")

    def setup_method(self):
        print("开始计算")

    def teardown_method(self):
        print("计算结束")



# 加法
    @pytest.mark.parametrize("a,b,expect",get_calculate()[0],ids=get_calculate()[4])
    def test_add(self,a,b,expect):
        res=self.cal.add(a,b)
        print(res)
        assert res==expect
# 减法
    @pytest.mark.parametrize("a,b,expect",get_calculate()[1],ids=get_calculate()[4])
    def test_subtract(self,a,b,expect):
        res=self.cal.subtract(a,b)
        print(res)
        assert res==expect
# 乘法
    @pytest.mark.parametrize("a,b,expect",get_calculate()[2],ids=get_calculate()[4])
    def test_multiply(self,a,b,expect):
        res=self.cal.multiply(a,b)
        print(res)
        assert res== expect
# 除法
    @pytest.mark.parametrize("a,b,expect",get_calculate()[3],ids=get_calculate()[4])
    def test_division(self,a,b,expect):
        res=self.cal.division(a,b)
        print(res)
        assert res==expect


if __name__=="__main__":
    pytest.main('test_calculate.py')