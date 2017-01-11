import os
def get_parent_host_name():
    host = os.popen("hostname -I|awk '{print $1}'")
    thost = host.read()
    host = thost.split('.')
    host = host[0:-1]
    server_host = ""
    for i in host:
        server_host += i + '.'
    server_host += '1'
    return server_host
print get_parent_host_name()


def sendnow():
    # ssh = os.popen("ssh root@192.168.12.206")
    IP = get_parent_host_name()
    print "IP: " + IP
    os.popen("scp /ack/Ack.txt" + " root@" + '192.168.12.1' + ":/ack")
    print 'Ack sent'

f = open("/ack/Ack.txt", 'w')
myMAC1 = os.popen("ifconfig | grep 'w' | awk '{print $5}'")  # get machine MAC
myMAC = myMAC1.read(17)  # proper MAC
print myMAC
files = os.popen('ls -t /erase/')
fname = files.read()
# fn=fname.split('\n')
print fname
w=myMAC + '->'+fname
print  'hello '+w
f.write(w)
f.close()
sendnow()
