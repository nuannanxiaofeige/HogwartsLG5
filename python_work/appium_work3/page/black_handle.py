# -*- coding:utf-8 -*-
import yaml


def black_handle(fun):
    def run (*args,**kwargs):
        instance=args[0]
        with open("../data/blacklist.yml","r",encoding="utf-8") as f:
            black_lists= yaml.load(f)
            # 捕获异常
            try:
                return fun(*args,**kwargs)
            except Exception as e:
                # 遍历黑名单
                for black in black_lists:
                    # 如果发现黑名单中的元素存在
                    eles = instance.driver.find_elements(*black)
                    # 对黑名单的元素进行处理
                    if len(eles) > 0:
                        # 通过点击的方式关闭
                        eles[0].click()
                        # 再次查找
                        return fun(*args,**kwargs)
                raise e
    return run


