import requests
import allure
import random
import json
import pytest
from commons.requests_util import Requestsutil
from commons.yaml_util import read_extract_yaml, read_testcase_yaml, write_extract_yaml


class TestProductApi:

    @pytest.mark.parametrize('args_name',read_testcase_yaml('/testcase/product_manage/test_get_token.yaml'))
    def test_get_token(self, args_name):
        #通过session会话取关联，session默认的情况下会自动关联cookie
        # session = requests.session()
            print('----------------')
            name =(args_name['name'])
            headers= (args_name['request']['headers'])
            validate =  (args_name['validate'])
            methods=(args_name['request']['method'])
            urls = (args_name['request']['url'])
            datas = (args_name['request']['datas'])

            res = Requestsutil('base_spgl_url').send_request(method=methods,url=urls, params=datas)
            print(res.json())
            write_extract_yaml({'access_token':res.json()['access_token']})
    #         # 返回 body 的 json 格式, 这是返回的就是 python 的字典格式
    #         TestProductApi.access_token = res.json()['access_token']


    @pytest.mark.parametrize('args_name', read_testcase_yaml('/testcase/product_manage/test_select_flag.yaml'))
    def test_select_flag(self,args_name):
            print('----------------')
            name = (args_name['name'])
            headers = (args_name['request']['headers'])
            validate = (args_name['validate'])
            methods = (args_name['request']['method'])
            urls = (args_name['request']['url'])
            datas = (args_name['request']['datas'])

            urls = urls+read_extract_yaml('access_token')
            res = Requestsutil('base_spgl_url').send_request('get',url=urls)
            print(res.json())

    @pytest.mark.parametrize('args_name', read_testcase_yaml('/testcase/product_manage/test_create_flag.yaml'))
    def test_create_flag(self,args_name):
                print('----------------')
                name = (args_name['name'])
                headers = (args_name['request']['headers'])
                validate = (args_name['validate'])
                methods = (args_name['request']['method'])
                urls = (args_name['request']['url'])
                datas = (args_name['request']['datas'])
                urls = urls + read_extract_yaml('access_token')
                res = Requestsutil('base_spgl_url').send_request(method =methods,url= urls, data=json.dumps(datas))
        #  # 将 uncode 编码转化成中⽂, 由于返回的 json 的 uncode 有两个斜杠, 所以需要替换为⼀个斜杠
                print(json.loads(json.dumps(res.json()).replace(r"\\", "\\")))
        #     TestProductApi.tag_id = res.json()["tag"]["id"]

        # def test_delete_flag(self):
        #     url = "/cgi-bin/tags/delete?access_token=" + TestProductApi.access_token
        #     datas = {"tag": {"id": TestProductApi.tag_id}}
        #     res = Requestsutil('base_spgl_url').send_request('post',url=url,data=json.dumps(datas))
        #     print(res.json())
        # def test_file_upload(self):
        #     url = "/cgi-bin/media/uploadimg?access_token=" + TestProductApi.access_token
        #     datas = {
        #   "media": open(r"D:\test.jpg", "rb")}
        #     res = Requestsutil('base_spgl_url').send_request('post',url=url,files=datas)
        #     print(res.json())