#  print("Hello"+" World!");
# word='dsa'
# while word=='dsa':
# 	i=i+1
# 	word='happy invincible why'
# 	pass
# print('%s %s' % (word[6:],i))
# print('is so '+word[0:5])


#  ***************************************************************************
# list=[]
# print(list[::-1])


# str={'why':"强无敌的巨佬","超级why":"天衣无缝之py极致"}
# a=input('请输入why或者超级why\n')
# print(str[a])


# a,b=60,13
# c=a&b
# print(c)

#  *****************************************************************************
# i=1
# while True:
# 	if i!=20:
# 		print(i)
# 		i+=1
# 	else:
# 		break
#  *****************************************************************************
# i = 2
# while(i < 100):
#    j = 2
#    while(j <= (i/j)):
#       if not(i%j):
#       	print("当i=%s,j=%s时j能整除i,所以%s存在因数%s" % (i,j,i,j))
#       	break
#       j = j + 1
#    if (j > i/j) : print('%s %s' %(i,"是素数"))
#    i = i + 1

#  **********************************************************************************
# print('请填写自己的姓名')
# a=input()
# print('请填写自己的年龄')
# b=input()
# print('大家好我叫%s,今年%s岁' %(a,b))

#  ************************************************************************************
# import time;
# a=time.asctime(time.localtime(time.time()))
# print(a[11:19])

#  ************************************************************************************
# import calendar
# a=calendar.month(2017,12)
# print(a)

#  ******************************************************************************
# import math;
# def calcb(num):
# 	a=math.sqrt(num);
# 	print("您输入的数字的平方根为 %s" %a);
# num=input('请输入一个数字:')
# try:
# 	float(num)
# except ValueError:
# 	print('请输入正确的数字')
# else:
# 	calcb(float(num));

#  ******************************************************************************
# var='sdsdsdsdsdABC'
# var=var.swapcase()
# print(var)


#  *******************************************************************************
# file=open("kl.txt","a+")
# file.write("个毛线")
# #file.seek(0,0)
# file.close()
# file=open("kl.txt","r+")
# file.write("呸")
# #file.close()
# #file=open("kl.txt","r")
# file.seek(0,0)
# var=file.read()
# file.close()
# print(var+"了")

#************************************************************************

# import socket
# import sys

# # 创建 socket 对象
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # 获取本地主机名
# host = socket.gethostname()

# # 设置端口好
# port = 9999

# # 连接服务，指定主机和端口
# s.connect((host, port))

# # 接收小于 1024 字节的数据
# msg = s.recv(1024)

# s.close()

# print (msg.decode('utf-8'))

#************************************************************************

# import random
# a=random.choice(range(1,101))
# num=input('请猜一个数字'+"\n")
# while(num!=a):
# 	try:
# 		num=int(num)
# 	except:
# 		print('请输入正确的数字！')
# 		num=input();
# 		continue;
# 	else:
# 		if(num>a):
# 			print('猜大了！')
# 			num=input();
# 		elif(num<a):
# 			print('猜小了！')
# 			num=input();
# 		else:
# 			break;
# print('你真tm叻仔！')

#************************************************************************

# import random
# import time

# class monster:
# 	def __init__(mon,name,can_catch,mon_run):
# 		mon.name=name
# 		mon.can_catch=can_catch
# 		mon.mon_run=mon_run

#************************************************************************

# 	def catch(mon):
# 		p_catch=random.choice(range(1,101))
# 		count=0
# 		while(count<5):
# 			count+=1
# 			if(p_catch>mon.can_catch):
# 				print('没抓到！')
# 				time.sleep(1)
# 				count=10
# 				break;
# 			else:
# 				if(count<4):
# 					p_catch=random.choice(range(1,101))
# 					print('摇！')
# 					time.sleep(1)
# 				else:
# 					break;
# 		if(count==4):
# 			print('成功了！抓到'+mon.name+'了！')
# 			return 1;
# 		else:
# 			return 0;

#************************************************************************

# 	def throw_rock(mon):
# 		mon.can_catch+=10
# 		mon.mon_run-=10

# 	def throw_food(mon):
# 		mon.mon_run+=10

# 	def if_run(mon):
# 		run=random.choice(range(1,101))
# 		if(run>mon.mon_run):
# 			print('野生的'+mon.name+'逃跑了')
# 			return 1
# 		else:
# 			return 0;




# def red_action(act,mon):
# 	flag=0;
# 	if(act=="1"):
# 		flag=mon.catch()
# 		if(flag==0):
# 			flag=mon.if_run();
# 	elif(act=="2"):
# 		print('小赤扔了石头，野生的'+mon.name+'害怕了！'+"\n")
# 		mon.throw_rock()
# 		time.sleep(1)
# 		if(flag==0):
# 			flag=mon.if_run();
# 	elif(act=="3"):
# 		print('小赤扔了食物，野生的'+mon.name+'更不容易逃跑了！'+"\n")
# 		mon.throw_food()
# 		time.sleep(1)
# 		if(flag==0):
# 			flag=mon.if_run();
# 	elif(act=="4"):
# 		print('小赤逃跑了!')
# 		flag=1
# 	else:
# 		print('请输入正确的数字！'+"\n")
# 		time.sleep(1)

# 	return flag;



# m=random.choice(range(1,4))
# if(m==1):
# 	mon1=monster("妙蛙种子",70,90);
# elif(m==2):
# 	mon1=monster("小火龙",70,90);
# elif(m==3):
# 	mon1=monster("杰尼龟",70,90);
# print('野生的'+mon1.name+'出现了！')
# flag=0;
# while(flag!=1):
# 	action=input('训练家小赤该怎么办？'+"\n"+'1:丢精灵球  2:丢石头'+"\n"+'3:丢食物  4:逃跑'+"\n")
# 	flag=red_action(action,mon1)
# 	if(flag==1):
# 		break;




# from flask import Flask,request,render_template
# from werkzeug.utils import secure_filename
# import os
# from _init_ import login_manager
# from _init_ import db,app

# blog = Blueprint('blog',__name__)

# @blog.route('/ppp/', methods = ['GET','POST'])
# def upload():
# 	return 'I\'m in py'




book = open("./123.txt")
line = book.readlines()
st = ''.join(line)
print(st)

