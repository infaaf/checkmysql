#!/usr/bin/env python3

import myfunctions as f
import pymysql
import time
from multiprocessing import Process;

servers = f.mysql_server_query(
    'select id,host,port,username,password,tags from base_clients_mysql where is_delete=0 and monitor=1;')

#print(servers)

def main():
    for server in servers:
        serverid = server[0]
        host = server[1]
        port = int(server[2])
        user = server[3]
        password = server[4]
        tags = server[5]
        #print(host,port,user,password)
        f.check_mysql_client(serverid,host,port,user,password,tags)
        print('aaaaaaaaaaa')

main()












