import pytest
import yaml

class TestData:
    @pytest.mark.parametrize(("a,b"),[(10,20),(30,40)])
    def test_data(self,a,b):
        print(a+b)

    # @pytest.mark.parametrize(("c,d"),yaml.safe_load(open("../config/data.yaml")))
    # def test_data2(self,c,d):
    #     print(c*d)



