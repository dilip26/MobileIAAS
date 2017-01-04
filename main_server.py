import os
import socket
import time

class NodeDiscovery:
    requiredNodes = 0
    temp = 0
    search = 1
    clients = 0
    port = 12345
    discoveredNodes = 0
    serverSocket = socket.socket()
    myClientsIP = []
    l = 0
    f = open("Paths.txt", "a+")

    def __init__(self):
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = self.getHostName()  # Get local machine name
        print 'intializing connection'
        self.serverSocket.bind((host, self.port))  # Bind to the port
        self.serverSocket.listen(100)

    def initialise(self):
        print "Requirements: "
        self.requiredNodes = int(input())
        self.clients = nd.list_clients()
        if self.clients == self.requiredNodes:
            print "Satisfied"
        else:
            print "Required Nodes: " + str(self.requiredNodes) + " and Clients: " + str(self.clients)
            self.temp += self.clients
            self.node_discovery()

    def ping_to_allUsers(self):
        for i in self.myClientsIP:
            os.popen("ping -c 1 " + i)
            print "Pinging to " + i + " ....."

    def node_discovery(self):
        self.discoveredNodes = self.server(self.clients)
        print "\nDiscovered Nodes : " + str(self.discoveredNodes) + "\n"
        self.temp += self.discoveredNodes
        criteria = self.requiredNodes - (self.temp)
        print "Criteria:" + str(criteria)
        if (criteria) > 1:
            self.search += 1
            time.sleep(5)
            print "\nSending Search :" + str(self.search)
            self.node_discovery()
        else:
            print "Satisfied"

    def verify_user(self, user):
        if str(user).find("none") == -1:
            return 1
        return 0

    def server(self, clients):
        discoveredClients = []
        print "Listening...."
        self.ping_to_allUsers()
        while clients != 0:
            c, addr = self.serverSocket.accept()  # Establish connection with client.
            print 'Got connection from', addr
            c.send(str(self.search))
            tmpDC = c.recv(2048)
            print "I got " + str(tmpDC)
            f = self.verify_user(tmpDC)
            if f == 1:
                dd = str(tmpDC).split("\n")
                self.l = len(dd)
                print "\nGot " + str(self.l) + " Clients"
                for i in dd:
                    discoveredClients.append(i)
                    self.f.write(i + "\n")
                    print "Write to file : " + str(i)
            print "Sent " + str(self.search) + " to " + str(clients) + " address ", addr
            c.close()
            clients -= 1

        return len(discoveredClients)

    def list_clients(self):
        x = os.popen('create_ap --list-client ap0')
        f = x.read()
        list = f.split('\n')
        f = 0
        clients = 0
        for i in list:
            if f != 0 and f < (len(list) - 1):
                ls = i.split()
                print "\nMy Clients :"
                print ls[1] + " " + ls[0]
                self.myClientsIP.append(ls[1])
                clients += 1
            f += 1
        return clients

    def getHostName(self):
        f = os.popen('ifconfig ap0|grep \'inet addr:\'|awk \'{print substr($2,6,length($2)-1)}\'')
        host = f.readline()
        return host[0:-1]


# MAIN
if __name__ == '__main__':
    nd = NodeDiscovery()
    nd.initialise()
