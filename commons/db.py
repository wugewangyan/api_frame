"""
存放本项目用的sql语句
"""

import pandas as pd
from sqlalchemy import create_engine
import pymysql
import psycopg2

db_dict = {
    #通风库
    # "datax_web": {
    #     "host": "124.65.131.14",
    #     "port": 23306,
    #     "user": "rhtect",
    #     "passwd": "rhtect@123.com"
    # },
    "watchdog": {
        "host": "124.65.131.14",
        "port": 1315,
        "user": "postgres",
        "passwd": "pwd@123"

}
    }
# 看门狗，数据库链接地址 PostgresSQL 192.168.10.50，链接库：watchdog，用户名：postgres/pwd@123

# ---- 用pymysql 操作数据库

    # conn=psycopg2.connect(host=host, port=port, db=datebasename, user=user, passwd=passwd, charset="utf8")
    # return conn

def dbconnect(host, user, datebase, passwd, port="1315"):

    conn = psycopg2.connect(host=host, port=port, db=datebase, user=user, passwd=passwd)
    return conn
# def dbconnect(host, user, datebasename, passwd, port="23306"):
#
#     conn = pymysql.connect(host=host, port=port, db=datebasename, user=user, passwd=passwd, charset="utf8")
#     return conn



def op(sql, datebase="watchdog"):
    host = db_dict[datebase]["host"]
    port = db_dict[datebase]["port"]
    user = db_dict[datebase]["user"]
    passwd = db_dict[datebase]["passwd"]
    conn = psycopg2.connect(host, user, datebase, passwd, port)
    # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
    cursor = conn.cursor
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.commit()

    # 关闭数据库连接
    cursor.close()
    conn.close()
    return results


# 初始化数据库连接
# 按实际情况依次填写MySQL的用户名、密码、IP地址、端口、数据库名
# engine = create_engine(
#     "mysql+pymysql://{}:{}@{}:{}/{}".format('root', 'AuTo!3%7', '10.168.100.156', '3306', 'seckill_platform_test'))


def engine(datebasename):
    return create_engine(
        "mysql+pymysql://{}:{}@{}:{}/{}".format('root', 'AuTo!3%7', '10.168.100.156', '3306', datebasename))



# 数据库查询
def query(sql_query, datebasename="assignment_platform_test"):
    # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    df_read = pd.read_sql_query(sql_query, engine(datebasename))
    # print(df_read["id"])
    return df_read


# 数据库操作
def operation(sql, datebasename="assignment_platform_test"):
    eng = engine(datebasename)
    conn = eng.connect()
    return conn.execute(sql)


# 创建活动第一期
def insert(data, datebasename, table):
    # DataFrame写入MySQL
    # 新建DataFrame
    df_write = pd.DataFrame(data)
    # 将df储存为MySQL中的表，不储存index列 todo 创建魔盒活动第一期
    df_write.to_sql(table, engine(datebasename), if_exists='append', index=False)

# if __name__ == '__main__':
