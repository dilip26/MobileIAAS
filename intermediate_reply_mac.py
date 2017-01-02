import os
import  socket


def get_host_name(): #method to get host name of current machine

    f = os.popen('ifconfig ap0|grep \'inet addr:\'|awk \'{print substr($2,6,length($2)-1)}\'') #will give host name
    host = f.read()
    return  host[0:-1]  #code to remove extra newline  char
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


def server(ip,count):   #code execujted when ip receive greater than 1
    ss=socket.socket()
    host = get_host_name()  # Get local machine name
    port = 12345  # Reserve a port for your service.
    ss.bind((host, port))  # Bind to the pohttps://www.youtube.com/watch?v=O1Q0pMeIZBwrt
    ss.listen(count) # it will wait untill all of its clients replay it
    print "Listening"
    myMAC1 = os.popen("ifconfig | grep 'w' | awk '{print $5}'") #get machine MAC
    myMAC = myMAC1.read(17) #proper MAC
    print myMAC
    clientips=""
    while count!=0:
        c, addr = ss.accept()
        print 'Got connection from', addr
        c.send(str(ip))
        clientips+=c.recv(1024)+"\n"
        count-=1
        c.close()
    clientips[0:-1] # to remove the extra newline char
    FinalMAC=""
    splitted=clientips.split('\n')
    splitted=splitted[0:-1]
    for i in splitted:
         FinalMAC+=myMAC+"->"+i+"\n"
    FinalMAC[0:-1]
    print  FinalMAC
    return FinalMAC

def list_client(sc):
    x = os.popen('create_ap --list-client ap0')
    f = x.read()
    count=0
    list = f.split('\n')
    finalMAC = ""
    myMAC1 = os.popen("ifconfig | grep 'w' | awk '{print $5}'")
    myMAC=myMAC1.read(17)
    mac = ""
    f = 0

    for i in list:
        if f != 0 and f < (len(list) - 1):
            ls = i.split()
            print ls[1] + " " + ls[0]
            mac = myMAC+"->"+ ls[0]
            finalMAC=finalMAC+mac+"\n"
            count += 1
        f += 1
    print count
    return finalMAC


sc = socket.socket()
sc.connect((get_parent_host_name(),12345))
print 'connected'
ip=sc.recv(1024)
print ip
ip=int(ip)
if(int(ip)==1):
    mac=list_client(sc)
    mac=mac[0:-1]
# myMAC = os.popen("ifconfig | grep 'w' | awk '{print $5}'")	# finalMAC= myMAC.read(17) + "->" + mac
    print mac
    sc.send(mac)
else:
    ip-=1
    c=os.popen('create_ap --list-clients ap0 | wc -l')
    count=c.read()
    count =count[0:-1]
    count=int(count)
    count-=1
    print count
    print 'new line'
    clients=server(ip,count)
    sc.send(str(clients))


'''ss=socket.socket()
host=socket.gethostname()
ss.bind((host,5555))
ss.listen(5)

c, addr = s.accept()

print 'Got connection from', addr

sc.send(mac)
c.send('Thank you for connecting')
c.close()'''
