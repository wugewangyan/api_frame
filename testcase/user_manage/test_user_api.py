import requests
from commons.requests_util import RequestsUtil
from commons.yaml_util import read_extract_yaml,write_extract_yaml
import re
class TestUserApi:
    pass

#     csrf_token = ""
# # 通过 session 会话去关联, session 默认的情况下回⾃动关联 cookie session = requests.session()
#
#     def test_phpwind_index(self,):
#         urls ="/phpwind/"
#         res = Requestsutil('base_yhgl_url').send_request("get", url=urls)
#         write_extract_yaml({'csrf_token': dict(res.cookies)['csrf_token']})
#  # TestWind.csrf_token = re.search('name="csrf_token" value="(.*?)"', res.text).group(1)
#  #        TestUserApi.csrf_token = dict(res.cookies)['csrf_token']
# # TestWind.phpwind_cookies = res.cookies
#         print(TestUserApi.csrf_token)
#
#     def test_phpwind_login(self):
#         urls = "/phpwind/index.php?m=u&c=login&a=dorun"
#         datas = {
#     "username": "admin",
#     "password": "msjy",
#     "csrf_token": read_extract_yaml('csrf_token'),
#     "backurl": "http://47.107.116.139/phpwind/",
#     "invite": ""
#                     }
#         headers = {
#     "Accept": "application/json",
#     "X-Requested-With": "XMLHttpRequest"
#  }
#         res = Requestsutil('base_yhgl_url').send_request("post", url=urls, data=datas, headers=headers)
#         print(res.json())