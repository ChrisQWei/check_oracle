#author: Chris
#email: christopherqiwei@gmail.com
#coding: utf8

import os
import datetime
import cx_Oracle
from CORE.input_output import input_io, output_io
from CORE.encrypt_decrypt import AESCipher
import re
import pandas as pd


class Check_database:

    def __init__(self, db_name, ip, username, password, instance_name, port):
        self.db_name = db_name
        self.ip = ip
        self.username = username
        self.password = AESCipher('mysecretpassword').decrypt(password)
        #self.password =password
        self.instance_name = instance_name
        self.port = port
        self.path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.result = []
    def _get_sql(self):
        with open(self.path+'/SQL/check_sql', 'r') as r:

            #sql_list = [ re.sub(';', '', x) for x in r.read()]
            sql_list = r.read().split(';')

        return sql_list

    def _save_result(self, result_list):
        dir_name = datetime.datetime.now().strftime('%Y-%m-%d')
        file_name = self.db_name + '_' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.csv'

        if os.path.exists(self.path+'/RESULTS/'+dir_name):
            dir = True
        else:
            os.mkdir(self.path+'/RESULTS/'+ dir_name)
            dir = True

        if dir:
            for results in result_list:
                if len(results) > 1:
                    factor_list = []
                    for num, result_dic in enumerate(results):
                        factor = 'a' + str(num)
                        factor = pd.DataFrame(result_dic, index=[factor])
                        factor_list.append(factor)

                    c = pd.concat(factor_list)
                    c.to_csv(self.path+'/RESULTS/'+ file_name, index=False, sep='\t', mode='a')

        return self.path+'/RESULTS/'+ file_name





    def _dictfetchall(self, cursor):
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


    def check(self):
        try:
            connect = cx_Oracle.connect(self.username, self.password,self.ip+':'+self.port+'/'+self.instance_name,
                                        mode=cx_Oracle.SYSDBA)
            cursor = connect.cursor()

        except cx_Oracle.DatabaseError as exc:
            error, = exc.args
            raise "Oracle-Error-Code:{}, Oracle-Error-Message:{}".format(error.code,
                                                                       error.message)

        if cursor:
            sql_list = self._get_sql()
            #print(sql_list)

            for i in sql_list:
                if len(i) > 3:
                    cursor.execute(i)
                    self.result.append(self._dictfetchall(cursor))
            cursor.close()
        if self.result:
            file_name = self._save_result(self.result)

        return file_name


