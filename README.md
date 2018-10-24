# check_oracle
Check oracle database status via python.

Environment required:
python 3.6
cx-Oracle       7.0.0
pandas          0.23.4
pycrypto        2.6.1

There are three steps to use this tool:
step1:
Install the toolkit which required.

If you can't "from Crypto.Cipher import AES" in python after you have installed the "pycrypto" via pip, then you should
use "easy_install pycrypto" by the way.

step2:
Add database information!
You can use below command to get the help instructions!
"python main_execute.py --help"
Follow the guide, add your database informations!

step3:
Now you can check database status!
You have to add check sqls manually in SQL/check_sql file. Keep the format same.
It's a simple command:
"python main_execute.py --operation=check"
Then choose the database which you want to check!
If check successfully, will return a csv file.


Enjoy!
If you have some sort of things,bugs or whatever, you can email me(christopherqiwei@gmail.com).



