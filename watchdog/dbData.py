import time
import pymysql
import psycopg2
#conn =
# pymysql.connect(host, user, password, database)

'''格式2'''
# db = pymysql.connect(host='124.65.131.14',port=23306,user="rhtect", password="rhtect@123.com", database="datax_web",charset='utf8')
# cursor = db.cursor()
# cursor.execute("select * from job_group")
# result = cursor.fetchall()
# for i in result:
#     print(i)
# print (type(cursor))
#1.连接数据库
# conn = pymysql.connect(
#     host='124.65.131.14',
#     port=23306,
#     user='rhtect',
#     password='rhtect@123.com',#密码
#     database='datax_web', #数据库名
#     charset='utf8'
# )
#2.创建游标对象
# cur = conn.cursor()
#3.对数据库进行CRUD操作
# try:
#     create_sqli = "create table hello (id int, name varchar(30));"
#     cur.execute(create_sqli)
# except Exception as e:
#     print("创建数据表失败:", e)
# else:
#     print("创建数据表成功;")
# #
# try:
#     insert_sqli = "insert into hello values(1, '杨将');"
#     cur.execute(insert_sqli)
# except Exception as e:
#     print("插入数据失败:", e)
# else:
#     conn.commit()
#     print("插入数据成功;")
# try:
#     cur.execute("select * from job_group")
#     result = cur.fetchall()
#     for i in result:
#         print(i)
# except Exception as e:
#     print("查询失败",e)
# else:
#     conn.commit()
#     print("查询数据成功;")
# # 4. 关闭游标
# cur.close()
# # 5. 关闭连接
# conn.close()

def db_datba(sql):
    conn = psycopg2.connect(
        host='124.65.131.14',
        port=1315,
        user='postgres',
        password='pwd@123',#密码
        database='watchdog', #数据库名
        # charset='utf8'
        )
    # 2.创建游标对象
    cur = conn.cursor()
    try:
        cur.execute(sql)
        data = cur.fetchall()
        # print(data)
    except Exception as e:
        print("查询失败",e)
    else:
        conn.commit()
    print("查询数据成功;")
    # 4. 关闭游标
    cur.close()
    # 5. 关闭连接
    conn.close()
    return data

# 通风测试库
# def link_databases(sql):
#     conn = pymysql.connect(
#         host='124.65.131.14',
#         port=23306,
#         user='rhtect',
#         password='rhtect@123.com',  # 密码
#         database='datax_web',  # 数据库名
#         charset='utf8'
#     )

    # cur = conn.cursor()
    # cur.execute(sql)
    # data = cur.fetchone()
    # return data
#
# if __name__ == '__main__':
# data=db_datba("select * from timer_config_table where id =131")
    # print(data)
    # data_id = 21
    # data = db_datba("SELECT * FROM job_jdbc_datasource WHERE id = {} ".format(data_id))
    # data_id = len(data) > 1 if len(data) < 1 else data[0][0]
    # print(data_id)
    #print(len(link_databases("SELECT id FROM job_jdbc_datasource WHERE datasource_name = 'api-ceshi1'")))