#author: Chris
#email: christopherqiwei@gmail.com
#coding: utf8

import os
import sys
import argparse
from CORE.encrypt_decrypt import AESCipher
from CORE.input_output import input_io, output_io
from CORE.check_db import Check_database

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--operation', type=str,
                        help='What operation?(check database , add or modify database information')
    parser.add_argument('--db_name', type=str,
                        help='This is a neccessary parameter whether you choose check , add or modify '
                             'infomations, by the way,'
                             'it must be unique!!')
    parser.add_argument('--ip', type=str, help='add or modify ip-address for a new or exists database ')
    parser.add_argument('--username', type=str, help='add or modify username for a new or exists database')
    parser.add_argument('--password', type=str, help='add or modify password for  a new or exists database. dont worry, '
                                                     'it will be encrypted '
                                                     'automately')
    parser.add_argument('--instance_name', type=str, help='add or modify instance_name for a new or exists database ')
    parser.add_argument('--port', type=str, help='add or modify port for a new or exists database')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    if args.operation == 'add':
        cipher = AESCipher('mysecretpassword')
        password = cipher.encrypt(args.password)
        a = input_io(args.db_name, args.ip, args.username, password, args.instance_name, args.port)
        if a == 0:
            return ("Add database:{} information succeed".format(args.db_name))
        elif a == 1:
            return ("Add database:{} information failed".format(args.db_name))

    elif args.operation == 'check':
        x = output_io('test', True)
        sys.stdout.write("db_options{}".format(x))
        y = input("Which database you want to chech(if more than one database just use comma to seperate the "
                  "db_name: ")
        try:
            db_name = y.split(',')
        except:
            db_name = [y]
        db_info = []
        if db_name:
            for i in db_name:
                db_info += output_io(i, False)

        if db_info:
            for i in db_info:
                a = Check_database(i['db_name'], i['ip'], i['username'], i['password'], i['instance_name'], i['port'])
                file_name = a.check()

            return "The result file is {}, please check!".format(file_name)

if __name__ == '__main__':
    main()