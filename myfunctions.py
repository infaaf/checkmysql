#!/usr/bin/env python3
import configparser
import pymysql
import time

#get config from conifig file
def  get_config(cfg_section,cfg_options):
    config = configparser.ConfigParser()
    config.read('server.cfg')
    config.value=config.get(cfg_section,cfg_options).strip('\"').strip('\'').strip(' ')
    return config.value


host=get_config('server','host')
port=get_config('server','port')
user=get_config('server','user')
password=get_config('server','password')
dbname=get_config('server','db')


# server
def mysql_server_query(sql):
    conn=pymysql.connect(host=host,user=user,password=password,port=int(port),db=dbname,connect_timeout=5,
                         charset='utf8')
  #  conn.select_db(dbname)
    cursor = conn.cursor()
    count=cursor.execute(sql)
    if count == 0 :
        result=0
    else:
        result=cursor.fetchall()
    return result
    cursor.close()
    conn.close()


def mysql_server_exec(sql,param):
    print(host)
    conn = pymysql.connect(host=host, user=user, password=password, port=int(port), db=dbname, connect_timeout=5,
                           charset='utf8')
    cursor = conn.cursor()
    if param != '':
        cursor.execute(sql,param)
    else:
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()







# to client
def check_mysql_client(serverid,host,port,user,password,tags):
    print("connecting"+host)
    try:
        conn=pymysql.connect(host=host,port=port,user=user,password=password,connect_timeout=1,charset='utf8')
        cursor=conn.cursor()
        cursor.execute("show global status")
        mysql_status = dict(cursor.fetchall())
        cursor.execute("show global variables")
        mysql_variables = dict(cursor.fetchall())
        print("connected and checking"+host)
        ### get status and store to db
        uptime=mysql_status['Uptime']
        version=mysql_variables['version']

        sql="insert into mysql_status(server_id,host,port,tags,uptime,version) values(%s,%s,%s,%s,%s,%s)"
        param = (serverid,host,port,tags,uptime,version)
        mysql_server_exec(sql,param)
        return  uptime



    except  pymysql.Error as e:
        print(e)






'''


conn = pymysql.connect(host='192.168.188.131',
                       user='python',
                       password='python',
                       db='test')

#def   get_conn(host,user,password,db):









def get_mysql_status():
    cur = conn.cursor()
    cur.execute("show global status")
    result = cur.fetchall()
    return result


def get_mysql_variables():
    cur = conn.cursor()
    cur.execute("show global variables")
    result = cur.fetchall()
    return result

'''

