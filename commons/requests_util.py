import json
import re

import jsonpath
import requests

from commons.str_util import replace_extract_param
from commons.yaml_util import read_config_yaml, write_extract_yaml, read_extract_yaml


class RequestsUtil():

    # 通过session会话去关联，session默认的情况下会自动关联cookie
    session = requests.session()

    def __init__(self, two_node):
        self.base_url = read_config_yaml('base', two_node)

    # 规范yaml用例 如果yaml配置合法， 返回True， 如果不合法， 我们返回False
    def standard_yaml(self, case_info):
        case_info_keys = case_info.keys()
        if 'name' in case_info_keys and 'request' in case_info_keys and 'validate' in case_info_keys:
            request_keys = case_info['request'].keys()
            if 'method' in request_keys and 'url' in request_keys:
                # print('YAML验证成功')
                return True
            else:
                print('在request下必须包含：method，url')
                return False
        else:
            print("一级关键字必须包含：name，request，validate")
            return False

    '''
    替换值的方法
    考虑问题1：（替换url，params，data，json，headers）
    考虑问题2：（string，int，float，list，dict）
    '''
    def replace_params(self, data):
        if data:
            # 1. 保存数据类型
            data_type = type(data)
            # 2. 判断数据类型, 转化成字符串
            if isinstance(data,dict) or isinstance(data,list):
                str_data = json.dumps(data)
            else:
                str_data = str(data)

            # 3. 替换参数
            str_data = replace_extract_param(str_data, "${", "}")

            # 4. 根据数据类型还原数据
            if isinstance(data,dict) or isinstance(data,list):
                data = json.loads(str_data)
            else:
                data = data_type(str_data)
        return data



    def extract_response(self, case_info, response):
        if 'extract' in case_info.keys():
            for key,value in case_info['extract'].items():
                if '(.*?)' in value or '(.+?)' in value:
                    zz_value = re.search(value, response.text)
                    if zz_value:
                        extract_value = {key:zz_value.group(1)}
                        write_extract_yaml(extract_value)
                else:
                    try:
                        resturn_json = response.json()
                        js_value = jsonpath.jsonpath(resturn_json,value)
                        if js_value:
                            extract_value = {key: js_value[0]}
                            write_extract_yaml(extract_value)
                    except Exception as e:
                        print('返回的结果不是json格式，不能使用json_path提取')


    # 处理请求
    def send_request(self, case_info):
        # 1. 验证yaml用例是否合法
        if not self.standard_yaml(case_info):
            print("yaml 配置验证【不合法】， 请修改后再试")
            return

        print("yaml 配置验证【合法】， 继续往下执行...")

        # 2. 获取发送请求必须的参数
        method = case_info['request'].pop('method')
        url = self.base_url + self.replace_params(case_info['request'].pop('url'))

        # 请求头和参数替换
        for key,value in case_info['request'].items():
            if key in ['params','data','json','headers']:
                case_info['request'][key] = self.replace_params(value)
            elif key == 'files':
                for file_key,file_path in value.items():
                    value[file_key] = open(file_path,'rb')
        # 3. 发送请求
        res = RequestsUtil.session.request(method, url, **case_info['request'])
        print(res.text)

        # 4. 处理响应
        self.extract_response(case_info, res)



        #包含断言
        def contains_assert(self,value,sj_value):
            flag = 0
            if str(value) not in str(sj_value):
                flag = flag+1
                print('断言失败：返回的结果中不包含' + str(value))
            return flag

    # # 统一封装请求
    # def send_request(self,method,url,**kwargs):
    #     #请求方法处理
    #     method = str(method).lower()
    #     #基础路径拼接
    #     url= self.base_url + url
    #     #请求
    #     res= Requestsutil.session.request(method,url,**kwargs)
    #     return res
