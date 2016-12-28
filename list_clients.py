import os

x=os.popen('ps aux|grep /usr/bin/create_ap')
f=x.readline().split()

x=os.popen('create_ap --list-client '+f[1])
f=x.read()

list=f.split('\n')

f=0
for i in list:
	if f!=0 and f<(len(list)-1):
		ls=i.split()
		print ls[1]+" "+ls[0]
	f+=1

