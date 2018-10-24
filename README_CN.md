# check_oracle
使用python进行oracle巡检

环境要求：
python 3.6
cx-Oracle       7.0.0
pandas          0.23.4
pycrypto        2.6.1

如何使用：
1.安装上述环境
如果通过 pip 安装pycrypto后， 无法 "from Crypto.Cipher import AES" , 您需要将pycrypto卸载，使用"easy_install pycrypto"
进行安装。

2.添加数据库信息
通过以下命令获取帮助
"python main_execute.py --help"
根据指引，进行添加

3.巡检数据库
打开SQL/check_sql，添加巡检sql，格式已经给出
使用如下命令，根据指引选择对应的数据库，
"python main_execute.py --operation=check"
如果检查成功，将返回巡检结果所在的CSV文件

祝使用愉快！
如果有任何问题，或者其他的，都可以给我发邮件哦(christopherqiwei@gmail.com)！
