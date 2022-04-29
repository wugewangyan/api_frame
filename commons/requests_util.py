import requests
from commons.yaml_util import read_config_yaml
class Requestsutil():

    def __init__(self,two_node):
        self.base_url = read_config_yaml('base',two_node)

    #通过session会话去关联，session默认的情况下会自动关联cookie
    session = requests.session()
#统一封装请求
    def send_request(self,method,url,**kwargs):
        #请求方法处理
        method = str(method).lower()
        #基础路径拼接
        url= self.base_url + url
        #请求
        res= Requestsutil.session.request(method,url,**kwargs)
        return res
