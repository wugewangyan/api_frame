import pytest
import time
import allure
from commons.yaml_util import read_yaml
import  requests

from testcase.father import Father
@allure.epic('接口测试自动化项目')
@allure.feature('用户登录接口')
class TestApi():
    # @pytest.mark.parametrize('args_name',['guoguo','hehe','haha'])
    @pytest.mark.parametrize('args_name',read_yaml('./testcase/user_manage/get_token.yaml'))
    def test_01_get_token(self,args_name):
        # time.sleep(2)
        print(args_name)


        names =args_name['name']
        reque =args_name['request']
        methods = args_name['request']['method']
        urls= args_name['request']['url']
        datas = args_name['request']['data']
        # headers =  args_name['request']['headers']
        # print(headers)
        res=requests.get(url=urls, data=datas)
        print(res)



    # def test_02_add_flag(self):
    #     time.sleep(2)
    #     print('增加标签接口')