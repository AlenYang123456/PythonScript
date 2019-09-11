#coding=utf-8
#!/usr/bin/ env python
"""
@作者：AllenQ
@文件名：AutoDeploy.PY
@时间：2019/9/12  0:16
@文档说明:
    Java项目 自动部署 脚本
"""

import os
import sys
import re
print("=======================Start======================")
print("springboot-docker-1.0.jar 启动脚本")
jar_name="springboot-docker-1.0.jar"             #1.指定要jar包的名称
dir_path="/root/"                                #2.指定要jar包放置的包路径
dest_path=dir_path+jar_name                      #3.拼装jar包的完成路径path
os.system("cp {} {}".format(jar_name,dest_path)) #4.将jar包复制到目标目录
cmd="jps -l |grep -v jps"                        #5.查看进程信息,判断该Java进程是否启动
ret1=os.popen(cmd)
list=ret1.readlines()
print(list)
for java_process_info in list:
    pid=java_process_info.split(" ")[0]              #6.获取进程id和进程名称
    pname=java_process_info.split(" ")[1]
    if re.findall(' (.*?)\.jar',java_process_info): #7.根据进程名判断Java进程是否启动
        os.system("kill " +str(pid))                 #8.杀掉该进程
        print("success kill process   {}" .format(java_process_info))
    break
os.system("nohup java -jar {} &".format(dest_path))
print("=======================End======================")
sys.exit(1)

