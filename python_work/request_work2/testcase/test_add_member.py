# -*- coding:utf-8 -*-
import pytest
from python_work.request_work2.api.address import Memeber


class TestCase():
    def setup(self):
        self.memeber=Memeber()

    def test_add_member(self):
        userid= '17712345686'

        # 添加联系人
        res=self.memeber.add_member(userid,name='李子789',mobile="17111111186",department=[1])
        pytest.assume(res.get('errcode') == 0)
        # print(f'res打印结果:{res}')

        # 查找联系人
        res=self.memeber.find_member(userid)
        pytest.assume(res.get('errcode')==0)
        # print(f'res打印结果:{res}')

        ## 更新联系人
        self.memeber.update_member(userid,name='张三zi',)
        pytest.assume(res.get('errcode')==0)
        # print(f'res打印结果:{res}')


        # 删除联系人
        res=self.memeber.delete_member(userid)
        pytest.assume(res.get('errcode')==0)
        # print(f'res打印结果:{res}')

        #
        # 查找联系人
        res=self.memeber.find_member(userid)
        pytest.assume(res.get('errcode')==60111)


if __name__== "__main__":
    pytest.main(["test_add_memeber.py","-sv"])



