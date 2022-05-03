import requests
import allure
import random
import json
from commons.yaml_util import read_extract_yaml
from commons.requests_util import RequestsUtil
import pytest
class TestApi():
    access_token=''
    # session = requests.Session()

    @allure.story("获取access_token") # 指定接⼝名称
    def test_index(self):
        url = "http://124.65.131.14:9080/open/account/api/base/auth/loginUser"
        res=RequestsUtil().send_request(method='get', url=url)
        data = {
            "?systemCode": "sys_code_04",
            "&_t": "ca",

    }
        # res = requests.get(url=url, params=data)
        print(res.json()) # 返回 body 的 json 格式, 这是返回的就是 python 的字典格式


    def test_login(self):
        url='http://124.65.131.14:9080/open/account/api/base/auth/login'

        data={
            'username': 'zengjuan',
            'password':'KJq7V+35XAMT1PlFgoN4wnlTfii6oFDIb/78Ecx3DQJvIjwjbtrlQwLLuMKnwgcYbTej8hirTiv4UrwZZl2fQgArjHspmj6u1GRMn8iQkSBRqG76UXc4ghyqK2SckMoW6PQ6w0bghSv/4bk5Ysg8H+BIfl/ULfk2/0ZC0g0MFGw='
        }
        res = RequestsUtil().send_request(method='post', url=url, json=data)
        # res = requests.post(url=url,json=data)
        print(res.json())



