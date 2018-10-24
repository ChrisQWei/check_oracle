#author: Chris
#email: christopherqiwei@gmail.com
#coding: utf8

import os

global path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def input_io(db_name, ip, username, password, instance_name, port):
    dic = {}
    dic['db_name'] = db_name
    dic['ip'] = ip
    dic['username'] = username
    dic['password'] = password
    dic['instance_name'] = instance_name
    dic['port'] = port
    try:
        with open(path+'/INFO/dbinfo', 'a') as w:
            w.writelines(str(dic)+'\n')
        return 0
    except:
        return 1


def output_io(db_name, return_name_only=True):
    db_name_list = ['all']
    return_list = []

    with open(path+'/INFO/dbinfo', 'r') as r:
        db_list = [ eval(x) for x in r.readlines()]
    if return_name_only:
        if db_list:
            for i in db_list:
                db_name_list.append(i['db_name'])

            return db_name_list
    else:
        if db_name == 'all':
            return db_list
        else:
            for db_info in db_list:
                if db_info['db_name'] == db_name:
                    return_list.append(db_info)

            return return_list




#input_io('test2','1.1','ss','ss','dd','123')
#x=output_io('test',False)
#print(x)