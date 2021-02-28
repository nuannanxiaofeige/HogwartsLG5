# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import requests

from python_work.request_work2.api.base import Api


class Memeber(Api):

    # 查找成员
    def  find_member(self,userid):
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}'
        return self.send("get",url)


    # 更新成员
    def update_member(self,userid,name,**kwargs):
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        body={
            "userid": userid,
            "name": name}
        return self.send('post',url,json=body,**kwargs)

    #添加成员
    def add_member(self,userid,name,mobile,department,**kwargs):
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        body={
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        return self.send('post',url,json=body,**kwargs)

    # 删除成员
    def delete_member(self,userid):
        url=f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}'
        return self.send('get',url)
