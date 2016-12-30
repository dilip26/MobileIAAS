import os,socket

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

serverSockect = socket.socket()  # Create a socket object
def server(clients):
    host = "192.168.12.1"  # Get local machine name
    port = 12345  # Reserve a port for your service.
    serverSockect.bind((host, port))  # Bind to the port
    serverSockect.listen(clients)
    print "Listening"

    while clients!=0:
        c, addr = serverSockect.accept()  # Establish connection with client.
        print 'Got connection from', addr
        c.send("1")
        myClients.append(c.recv(1024))
        # print clients
        clients-=1
        c.close()
    return c
    # print c.recv(1024)
    # c.send('Thank you for connecting')
    # c.close()

print "Requirements: "
nodes = int(input())
t = 0
f = open("Paths.txt","r+")
clients = list_clients()
if (nodes - clients) > 0:
    print clients
    c = server(clients)
    # print myClients
    data = f.readline()
    # for d in data:
    # print data
    # c = 1
    for i in myClients:
        # for d in data:
        #     d.find(c)
        #     c += 2
        f.write(str(i)+'\n')