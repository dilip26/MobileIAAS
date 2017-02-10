import os


def getip():
    f = 0
    for i in list:
        if f != 0 and f < (len(list) - 1):
            ls = i.split()
            print ls[0] + "   " + ls[1]
            print "LS[0]:" + ls[0] + " TEMP: " + str(temp[0]).replace("_", ":")
            if str(ls[0]).find(str(temp[0])):
                return ls[1]
        f += 1
    return 1

files = os.listdir('/erase/')
print 'waiting'

while len(files) == 0:
    files = os.listdir('/erase/')
print files[0]
tokens = files[0].split('+')
print tokens[1]
if len(tokens) == 2:
    print "in storage "
    os.popen("scp /erase/" +files[0] + " root@192.168.12.1:/ack")
    os.rename("/erase/"+files[0], "/storage/" + tokens[1])
    print "ack sent"
else:
    print 'I came in else '
    newname = ""
    i = 1
    c = len(tokens)
    while c > 1:
        newname += tokens[i] + "+"
        i += 1
        c -= 1

    print "rename file:" + str(newname[0:-1])
    print files[0]
    os.popen('mv /erase/'+files[0]+' /erase/'+newname[0:-1])
    # os.rename("/erase/"+files[0], "/erase/"+newname[0:-1])
    temp = str(newname[0:-1]).split("+")
    print "mac to obtain ip:" + str(temp[0])
    x = os.popen('create_ap --list-client ap0')
    f = x.read()
    list = f.split('\n')
    # os.popen("scp /erase/" + files[0] + " root@192.168.12.1:/ack")
    a = getip()
    if a != 1:
        print "ip of destination" + str(a)
        print "scp /erase/" + str(newname[0:-1]) + " root@" + str(a) + ":/erase"
        os.popen("scp /erase/" + str(newname[0:-1]) + " root@" + str(a) + ":/erase/")
        os.remove('/erase/'+str(newname[0:-1]))
