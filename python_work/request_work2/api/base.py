# -*- coding:utf-8 -*-
import requests


class Api:
    def __init__(self):
        # 获取token
        corpid='ww76241eb39c2799cb'
        corpsecret='f8Lf_3Chtbafwy41Gxb3iI5Gn6tBmTx7kLrse5fdjUI'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
        r=requests.get(url)
        self.token=r.json()["access_token"]

        # 将获取到的token放到session中
        self.session=requests.session()
        self.session.params={'access_token':self.token}



    def send(self,*args,**kwargs):
        # 需传入位置参数和关键词参数,()位置参数可传多个，关键字参数只可传入一个
        res=self.session.request(*args,**kwargs)
        return res.json()