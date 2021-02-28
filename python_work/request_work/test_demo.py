# -*- coding:utf-8 -*-
import requests


# 获取token
url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww76241eb39c2799cb&corpsecret=f8Lf_3Chtbafwy41Gxb3iI5Gn6tBmTx7kLrse5fdjUI'
a = requests.get(url)
token=a.json()['access_token']
# print(token)

# 查询成员
url=f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=LiZi'
b = requests.get(url)
# print(b.json())

# 更新成员
url=f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}'
body={
    "userid": "LiZi",
    "name": "张三1234"}
c = requests.post(url,json=body)
# print(c.json())

#添加成员
url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}'
body={
    "userid": "1771234568",
    "name": "张zhang",
    "mobile": "17212345678",
    "department": [1,2]
}
r=requests.post(url,json=body)
# print(r.json())

# 删除成员
url=f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=1771234568'
d = requests.get(url)
# print(d.json())
