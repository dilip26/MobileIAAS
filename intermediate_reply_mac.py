import os
import  socket

def list_client(sc):
	x = os.popen('create_ap --list-client ap0')
	f = x.read()
	list = f.split('\n')
	mac = ""
	f = 0
	count = 0
	for i in list:
		if f != 0 and f < (len(list) - 1):
			ls = i.split()
			print ls[1] + " " + ls[0]
			mac = mac + ls[0] + " "
			count += 1
		f += 1
	print count
	return mac

sc = socket.socket()
sc.connect(("192.168.12.1",12345))
print 'connected'
ip=sc.recv(1024)
print ip
ip=int(ip)
if(int(ip)==1):
	mac=list_client(sc)
	myMAC = os.popen("ifconfig | grep 'w' | awk '{print $5}'")
	finalMAC= myMAC.read(17) + "->" + mac
	# print finalMAC
	sc.send(finalMAC)
else:
	ip-=1
	print 'req sent to the user'

'''ss=socket.socket()
host=socket.gethostname()
ss.bind((host,5555))
ss.listen(5)

c, addr = s.accept()

print 'Got connection from', addr

sc.send(mac)
c.send('Thank you for connecting')
c.close()'''
