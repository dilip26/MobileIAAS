import os

class FileStorage:
    file = open("Paths.txt", "r")
    path = file.read().split('\n')
    mac = ''
    # path1 = file.read().replace(":", "_").split('\n')
    def initialise(self):
        print "To whom file is to be sent "
        self.mac = raw_input()
        self.SendFile()

    def SendFile(self):
        print "find:" + str(self.mac)
        for i in self.path:
            if i.find(self.mac) == -1:
                print str(i)
            else:
                # print "else:" + str(i)
                self.final(i)
                break

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
                m = self.mac.split("+")
                print "Comparing :" +ls[0] + " with " + m[0]
                if ls[0] == m[0]:
                    return ls[1]
            f += 1
        return "IP not found"

    def sendnow(self, filetosend):
        # ssh = os.popen("ssh root@192.168.12.206")
        IP = self.list_clients()
        if IP == "IP not found":
            print "Unable to send because IP not found"
        else:
            print "IP: "+IP
            print "Sent file: "+str(filetosend)
            os.popen("scp " + str(filetosend) + " root@"+IP+":/erase")
        f = open("xyz.txt.p_0", 'w')

    def final(self, pathtosend):
        print "pathtosend : " + str(pathtosend)
        pathtosend = str(pathtosend).replace(":", "_")
        # pathtosend = str(pathtosend).replace("->", "+")
        print "pathtosend replaced: " + str(pathtosend)
        e = 0
        os.rename("xyz.txt.p_" + str(e), str(pathtosend) + "+xyz.txt.p_" + str(e))
        print "xyz.txt.p_" + str(e), str(pathtosend) + "+xyz.txt.p_" + str(e)
        print str(pathtosend)
        self.sendnow(str(pathtosend) + "+xyz.txt.p_" + str(e))
        # e += 1


if __name__ == '__main__':
    m = FileStorage()
    m.initialise()
    # print m.list_clients()
