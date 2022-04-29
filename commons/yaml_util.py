import yaml
import os
#获取项目根目录
def get_object_path():
    print(os.getcwd())
    return os.getcwd()
#读取extract.yaml文件
def read_extract_yaml(key):
    with open(get_object_path()+'/extract.yaml',encoding='utf-8') as f:
       return yaml.load(stream=f,Loader=yaml.FullLoader)[key]

#写入extract.yaml文件
def write_extract_yaml(data):
    with open(get_object_path()+'/extract.yaml',encoding='utf-8',mode='a') as f:
        yaml.dump(data=data, stream=f, allow_unicode =True)
    #清空
def clear_extract_yaml():
        with open(get_object_path() + '/extract.yaml', encoding='utf-8', mode='w') as f:
            f.truncate()
#读取config.yaml
def read_config_yaml(one_node,two_node):
    with open(get_object_path()+'/config.yaml',encoding='utf-8') as f:
       return yaml.load(stream=f,Loader=yaml.FullLoader)[one_node][two_node]
#读取测试用例的yaml
def read_testcase_yaml(yaml_path):
    with open(get_object_path()+yaml_path,encoding='utf-8') as f:
       return yaml.load(stream=f,Loader=yaml.FullLoader)
