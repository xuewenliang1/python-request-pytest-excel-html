import requests
import json
from log import log
class method(object):
    def get(self, url, heraders=None, data=None):
        if heraders is not None:
            rq = requests.get(url, headers=heraders, params=data)
        else:
            rq = requests.get(url, params=data)
        return rq

    def post(self, url, headers=None, data=None):
        if headers is not None:
            rq = requests.post(url, headers=headers, data=data)
        else:
            rq = requests.post(url, data=data)
        return rq

    def run_method(self, method, url, headers=None, data=None):
        if method == "get" or "GET":
            rq = self.get(url, headers, data)

        elif method == "post" or "POST":
            rq = self.post(url, headers, data)

        else:
            rq = "请求方式不正确"
        log.write_debug(rq.text)
        return rq



