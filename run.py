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