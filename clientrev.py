import os

def getmac(mac):
    mac = mac.split('\n')
    x = os.popen('create_ap --list-client ap0')
    f = x.read()
    ls = ''
    ip = ''
    list = f.split('\n')
    f = 0
    for i in list:
        if f != 0 and f < (len(list) - 1):
            ls = i.split()
            if ls[0] == mac[0]:
                ip += ls[1] + ' '
        f += 1
    return ip

files = os.listdir('/ping/')
while len(files) == 0:
    # print files
    files = os.listdir('/ping')
# print files[0]
# files = "pingingPath.txt"
pingpath = open("/ping/" + files[0], "r")
r = pingpath.readline()
while len(r) == 0:
    pingpath = open("/ping/" + files[0], "r")
    r = pingpath.readline()
print r
pingpath.close()
print r
content = r.split("+")
print content
if len(content) == 2:
    print "searching the file " + content[1] + " in storage folder and sending it to the server........"
    print content[1]
    if os.path.exists("/storage/" + content[1]):
        os.popen("scp /storage/" + content[1] + " root@192.168.12.1:/retrieved")  # Sending file to the server directly
        print "scp /storage/" + content[1] + " root@192.168.12.1:/retrieved"
else:
    file1 = open("/ping/pingingPath.txt", "w")
    del content[0]
    ip = getmac(content[0])
    print ip
    p = '+'.join(content)
    print p
    file1.write(p)
    file1.close()
    os.popen("scp /ping/pingingPath.txt root@" + ip[0:-1] + ":/ping")
    print "scp /ping/pingingPath.txt root@" + ip[0:-1] + ":/ping"
os.remove('/ping/pingingPath.txt')
