import pytest
import yaml

class TestDemo:
    @pytest.mark.打印标题1
    @pytest.mark.parametrize("env",yaml.safe_load(open("../config/env.yaml")))
    def test_demo(self,env):
        if "ip" in env:
            print("这是测试环境")
            print(f"测试环境的ip是：{env['ip']}")
        elif "dev" in env:
            print("这是开发环境")
    @pytest.mark.打印标题2
    def test_yaml(self):
        print(yaml.safe_load(open("../config/env.yaml")))

