import os,socket
search = "1"
myClients = []
def list_clients():
    x = os.popen('create_ap --list-client ap0')
    f = x.read()
    list = f.split('\n')
    f = 0
    clients = 0
    for i in list:
        if f != 0 and f < (len(list) - 1):
            ls = i.split()
            print ls[1] + " " + ls[0]
            clients+=1
        f += 1
    return clients

def getHostName():
    f = os.popen('ifconfig ap0|grep \'inet addr:\'|awk \'{print substr($2,6,length($2)-1)}\'')
    host = f.readline()
    return host[0:-1]

serverSockect = socket.socket()  # Create a socket object
def server(clients):
    host = getHostName()  # Get local machine name
    print host
    port = 12345  # Reserve a port for your service.
    serverSockect.bind((host, port))  # Bind to the port
    serverSockect.listen(clients)
    print "Listening"

    while clients!=0:
        c, addr = serverSockect.accept()  # Establish connection with client.
        print 'Got connection from', addr
        c.send(search)
        myClients.append(c.recv(1024))
        print clients
        c.close()
        clients-=1

    return len(myClients)
    # print c.recv(1024)
    # c.send('Thank you for connecting')
    # c.close()

print "Requirements: "
requiredNodes = int(input())
t = 0
f = open("Paths.txt","r+")
clients = list_clients()
discoveredNodes = server(clients)
if (requiredNodes - (discoveredNodes+clients)) > 0:
    print clients
    # print myClients
    # data = f.readline()
    # for d in data:
    print discoveredNodes
    # c = 1
    for i in myClients:
        # for d in data:
        #     d.find(c)
        #     c += 2
        f.write(str(i)+'\n')