import sys

import requests
import yaml
import yaml
import os
base_path=os.getcwd()
sys.path.append(base_path)
#获取项目根目录
def get_object_path():
    print(os.getcwd())
    return os.getcwd()

# host = 'http://124.65.131.14:9082/'
host ='http://124.65.131.14:9080/'
session = requests.session()

def login():
    url = host + 'open/account/api/base/auth/login'
    data ={
    "username":"zengjuan",
    "password":123456
}
    re = session.request(method = 'POST',url = url,json= data)
    auth = re.headers["Authorization"]
    # print(re.headers)
    # print(re.json())
    # print(auth)
    return auth

def write_yaml(auth):
    auth = {"auth":auth}

    with open('./token.yaml',encoding='utf-8',mode='a') as f:
        yaml.dump(data = auth,stream=f,allow_unicode=True)

def read_yaml():
    with open('./token.yaml',encoding='utf-8',mode='r') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
        auth = result["auth"]
        return auth

def delete_watchdog():
    auth = read_yaml()
    headers = {'Authorization':auth
               }
    url = host + 'api/open/watchdog/v1/config'
    data = {
        'id': 423
    }
    re = session.request(method='DELETE', url=url, data =data,headers =headers)
    print(re.json())







if __name__ == '__main__':
    # auth=login()
    # write_yaml(auth)
    # read_yaml()
    delete_watchdog()