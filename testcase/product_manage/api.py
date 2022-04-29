import time
import pytest
import requests
import allure
# from testcase.father import Father

# @pytest.fixture(scope ='function')
# def test_sql():
#     print('test_sql')
#     yield '测试'
#     print('test_sql')
# @pytest.mark.usefixtures('execute_sql')
# @allure.epic('接口测试自动化项目')
# @allure.feature('用户登录接口')
#
# class TestApi():
#     @allure.story('测试模块')
#     # @allure.title('打印地址')
#     @allure.severity(allure.severity_level.TRIVIAL) #严重程度
#     @allure.link('接口访问地址')
#     @allure.issue('bug链接')
#     @allure.testcase('测试用例的链接')
#     def test_02_guoguo(self,base_url,pro):
#         allure.dynamic.title(pro + '测试模块====')
#         allure.dynamic.description('测试用例的描述')
#         print('测试模块')
#         print(base_url+'-----------'+ pro)
#         # assert 'a' in 'ac'
#         requests.get(url = base_url +'/open/account/')
#         #步骤
#         for a in range(1,6):
#             with allure.step('执行第' + str(a) + '个步骤'):
#                 pass
#        # 附件
#         with open(r'D:\\test.jpg',mode='rb') as f:
#             content = f.read()
#             allure.attach(body=content,name='测试模块错误的截图',attachment_type=allure.attachment_type.JPG)
#         #文本
#         allure.attach(body ='接口地址：www.baidu.com',name ='这是一个文本附件',attachment_type=allure.attachment_type.txt)
#
#
#     @allure.story('测试模块1')
#     @allure.title('打印地址1')
#     def test_01_hehe(self):
#          print('hello')
# class TestApp():
#     def test_01_wan(self,test_sql,execute_sql):
#         print('haha')
#     def test_01_wanshua(self):
#         print('zouzou')



