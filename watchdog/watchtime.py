import  requests
import json

import datetime
import  time



host = 'http://124.65.131.14:9082/'
session = requests.session()
auth=''

def login(username,password):
    url = host + 'open/account/api/base/auth/login'
    data = {
        "username": username,
        "password": password,
    }
    re = session.request(method = 'POST',url = url,json= data)
    # print(re.json())
    # print(re.headers)
    global auth
    auth = re.headers['Authorization']
    # print(auth)

def add_wathchdog(name, startDate,endDate,warnInterval,warnVal,rateUnit,rateVal,restTime):

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
    '''
    data = {
        "id":79,
        "name":name,
        "rateInterval": 1,
        "warnInterval": warnInterval,
        "warnUrl":"http://oa.rhtect.com:808/seeyon/main.do?method=main",
        "warnVal": warnVal,
        "rateUnit": rateUnit,
        "startDate": startDate,
        "endDate": endDate,
        "rateType":2,
        "rateVal": rateVal,
        "bizStatus": 1,
        "restTime": restTime
    }
    re = session.request(method='POST', url=url,json = data,headers=headers)
    print(re.json())


def wa():
    url = host + 'api/open/watchdog/v1/config?keyword=&sourceType=&source=&bizStatus=&page=1'
    headers = {
        "Authorization": auth
    }
    re = session.request(method='GET', url=url ,headers=headers)
    # print(re.json())
    print(re.json()['body'])
    global uuid,id
    uuid =(re.json()['body']['records'][0]['uuid'])
    id = (re.json()['body']['records'][0]['id'])
    # print(id)


def clear():
    url = host +'api/open/watchdog/v1/callback/'+uuid
    print(uuid)
    headers = {
        "Authorization": auth
    }
    re = session.request(method='GET', url=url ,headers=headers)
    print(re.text)



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
    add_wathchdog('1111', '2022-05-16T16:00:00.000Z', '2022-05-19T16:00:00.000Z',0,0,2,'01,03',['2022-05-20'])

    # # add_wathchdog('nannana','2022-05-19T16:00:00.000Z','2022-05-19T16:00:00.000Z')
    wa()
    clear()
    # edit_time('2022-05-16','2022-05-19')
    # times()
