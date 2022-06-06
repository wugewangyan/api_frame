import dbm
import allure
import pytest


import  requests

import json

import datetime
import  time
from  commons import  db
from watchdog import dbData


host = 'http://124.65.131.14:9082/'
# host ='http://124.65.131.14:9080/'
session = requests.session()
auth=''

def sql1():
    data = dbData.db_datba("select * from timer_config_table where id =131")
    print(data)

def login(username,password):
    url = host + 'open/account/api/base/auth/login'
    data = {
        "username": username,
        "password": password,
    }
    re = session.request(method = 'POST',url = url,json= data)
    print(re.json())
    # assert re.status_code ==200
    print(re.headers)
    global auth
    auth = re.headers['Authorization']
    # print(auth)

def add_wathchdog(name, startDate,endDate,warnInterval,warnVal,rateInterval,rateUnit,rateVal,restTime):
    url = host + 'api/open/watchdog/v1/config'
    headers = {
        "Authorization": auth
    }
    # print(headers)

    '''
    1,ratetype=1频率是不重复，2频率是重复的
    2,warnInterval:告警值
    3，restTime：休息时间【2022-05-16，2022-05-18】
    5，bizStatus =1启用，0停用
    7，rateInterval：重复值，type为1，值为空，type为2，值为2，频率值
    8，rateUnit：重复单位小时1，天2，周3，月4，年5
    9，rateVal：频率值，小时，分钟（00，02，59），天小时（00-23），周一（00时，02时），月天（1-31），年月（1-12）
    10，warnVal：逾期告警值单位s
    add_wathchdog('1111', '2022-05-16T16:00:00.000Z', '2022-05-19T16:00:00.000Z',2,'',1,'01,03',['2022-05-20'])
    '''
    data = {
        "name":name,
        "rateInterval": rateInterval,
        "warnInterval": warnInterval,
        "warnUrl":"http://oa.rhtect.com:808/seeyon/main.do?method=main",
        "warnVal": warnVal,
        "rateUnit": rateUnit,
        "startDate": startDate,
        "endDate": endDate,
        "rateType": 2,
        "rateVal": rateVal,
        "bizStatus": 1,
        "restTime": restTime
    }
    re = session.request(method='POST', url=url,json = data,headers=headers)
    print(re.text)


def wa():
    url = host + 'api/open/watchdog/v1/config?keyword=&sourceType=&source=&bizStatus=&page=1'
    headers = {
        "Authorization": auth
    }
    re = session.request(method='GET', url=url ,headers=headers)
    print(re.json())
    # print(re.json()['body'])
    global uuid,id,name
    uuid =(re.json()['body']['records'][1]['uuid'])
    id = (re.json()['body']['records'][1]['id'])
    records = (re.json()['body']['records'][1])
    name =(re.json()['body']['records'][1]['name'])
    print(name)
    print(id)
    print(records)
def edit_watchdog():
    url = host + 'api/open/watchdog/v1/config'
    headers = {
        "Authorization": auth
    }
    data={"id":395,"name":"ggg","uuid":"f817826ac4f24b1ea9a8d6daf7d81e23",
          "effectDate":["2022-05-24T16:00:00.000Z","2022-07-30T16:00:00.000Z"],
          "rateInterval":2,"rateUnit":"2","warnInterval":22,"warnUrl":"https://www.baidu.com",
          "warnVal":'',"expire":0,"startDate":"2022-05-26T16:00:00.000Z",
          "endDate":"2022-07-30T16:00:00.000Z","rateType":"2","rateVal":"00,05","bizStatus":0,"restTime":["2022-07-03"]}
    re = session.request(method='PUT', url=url, json=data,headers=headers)
    print(re.text)


def clear():
    url = host +'api/open/watchdog/v1/callback/'+uuid

    # print(uuid)
    headers = {
        "Authorization": auth
    }
    #函数重复调用两次
    if name == '1' or name == '2':
        # 函数重复调用两次
        for _ in range(2):
            re = session.request(method='GET', url=url, headers=headers)
            print('执行2次----------'+re.text)
    else:
        re = session.request(method='GET', url=url, headers=headers)
        print('执行一次--------------'+re.text)



def edit_time(startDate,endDate):
    url = host +'api/open/watchdog/v1/modifyDate?id='+ str(id) + "&startDate="+ startDate +'&endDate='+endDate
    # print(id)
    headers = {
        "Authorization": auth
    }
    re = session.request(method='PUT', url=url ,headers=headers)
    print(re.text)


# def times():
#     utc_data1 = '2022-05-16'
#     utc_date2 = datetime.datetime.strptime(utc_data1, "%Y-%m-%d")
#     local_date = datetime.datetime.strftime(utc_date2, "%Y-%m-%dT%H:%M:%S.000Z")
#     print(local_date)

if __name__ == '__main__':
  login('zengjuan', 123456)

  # # add_wathchdog('1111','2022-05-16T16:00:00.000Z','2022-05-16T16:00:00.000Z',5,'',1,1,'01,02',[])
    # # #
    # # # # # add_wathcdog('nannana','2022-05-19T16:00:00.000Z','2022-05-19T16:00:00.000Z')
    # wa()
    #
    # clear()
    # # edit_time('2022-05-17','2022-05-19')
    # # times()
    # sql1()
  edit_watchdog()
