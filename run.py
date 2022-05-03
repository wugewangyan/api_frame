import  pytest
import  time
import os
from commons.yaml_util import read_extract_yaml


if __name__ == '__main__':
    # print(read_extract_yaml())
    pytest.main()
    # time.sleep(3)
    # os.system('allure generate ./temps -o ./reports --clean')
    #获取当前时间
    # times=time.strftime('%Y_%m_%d %H_%M_%S',time.localtime())
    #在reports文件下生成report开头的报告文件
    # os.system('allure geerate ./temps -o ./reports/report_'+ times + '--clean')

    # str = "/cgi-bin/tags/create?access_token=${adbddd}&a=${sss}"
    # if "${" in str and "}" in str:
    #     start_index = str.index("${")
    #     end_index = str.index("}",start_index)
    #     old_value = str[start_index:end_index+1]
    #     new_value = read_extract_yaml(old_value[2:-1])
    #     str = str.replace(old_value,new_value)
    #     print(old_value,new_value)
    #     print(str)
