import pytest

class TestClass():
    def setup_class(self):
        print("\n所有用例执行前")
    def teardown_class(self):
        print("\n所有用例结束后")

    def setup_method(self):
        print("\nsetup_method:每个用例前执行一次")
    def teardown_method(self):
        print("\nteardown_method:每个用例结束后执行一次")

    def test_one(self):
        print("正在执行：test_one")
    def test_two(self):
        print("正在执行：test_two")