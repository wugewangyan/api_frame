# import json
# import yaml
# import os
# #读取测试用例yaml
# from commons.yaml_util import get_object_path
#
#
# def read_testcase_yaml(yaml_path):
#     with open(get_object_path()+yaml_path,encoding='utf-8') as f:
#         case_info = yaml.load(f,Loader=yaml.FullLoader)
#         if len(case_info) >=2:
#             return case_info
#         else:
#             if "parameterize" in dict(*case_info).keys():
#                 new_case_info = ddt(*case_info)
#                 return new_case_info
#             else:
#                 return case_info
#
#
#
#
# def ddt(case_info):
#     if "parameterize" in case_info.keys():
#         case_info_str = json.dumps(case_info)
#         for param_key,param_value in case_info["parameterize"].items():
#             key_list = param_key.split('-')
#             length_flag = True
#             data_list = read_data_yaml(param_value)
#             for data in data_list:
#                 if len(data) != len(key_list):
#                     length_flag = False
#                     break
#             new_case_info = []
#             if length_flag:
#                 # 循环数据行数
#                 for x in range(1,len(data_list)):
#                     print("x=" + str(x))
#                     temp_case_info = case_info_str
#                     # 循环数据列数
#                     for y in range(0,len(data_list[x])):
#                         print("y=" + str(y))
#                         if data_list[0][y] in key_list:
#                             # 替换原始的yaml文件里的$ddt{}
#                             if isinstance(data_list[x][y],int) or  isinstance(data_list[x][y],str):
#                                temp_case_info = temp_case_info.replace('"$ddt{' + data_list[0][y]+'}"',str(data_list[x][y]))
#                             else:
#                                 temp_case_info = temp_case_info.replace("$ddt{" + data_list[0][y]+"}",str(data_list[x][y]))
#                     new_case_info.append(json.loads(temp_case_info))
#             return new_case_info
#     else:
#         return  case_info