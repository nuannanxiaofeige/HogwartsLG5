# -*- coding:utf-8 -*-


from mitmproxy import ctx
from mitmproxy import http


class ABC:
    def __init__(self):
        self.num = 0
    def request(self, flow: http.HTTPFlow) -> None:
        if "v5/stock/batch/quote.json" in flow.request.pretty_url:
          with open(r"C:\Users\Administrator\Desktop\tmp.json", 'r', encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )

addons = [
    ABC()
]


