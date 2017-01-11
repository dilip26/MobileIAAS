import os

files=os.listdir('/erase/.')
print 'waiting'
while(len(files)==0):
    files = os.listdir('/erase')
print files[0]
tokens=files[0].split('+')
print tokens[1]
if len(tokens)==2:
    print os.getcwd()
    os.chdir("/erase")
    print "in storage "
    os.rename(files[0],"/storage/"+tokens[1])
    os.system('python Ack.py')
else:
    newname = ""
    i = 1
    c=len(tokens)
    while c>1:
        newname += tokens[i]+"+"
        i += 1
        c = c -1
    os.chdir("/erase")
    print "rename file:"+str(newname[0:-1])
    os.rename(files[0],newname[0:-1])
    temp=str(newname[0:-1]).split("+")
    print "mac to obtain ip:"+str(temp[0])
    x = os.popen('create_ap --list-client ap0')
    f = x.read()
    list = f.split('\n')

    def getip():
        f = 0
        for i in list:
            if f != 0 and f < (len(list) - 1):
                ls = i.split()
                print ls[0] +"   "+ ls[1]
                print "LS[0]:"+ls[0]+" TEMP: "+str(temp[0]).replace("_",":")
                if str(ls[0]).find(str(temp[0])):
                    return ls[1]
            f += 1
        return 1


    a = getip()
    if a!=1:
        print "ip of destination"+str(a)
        os.popen("scp "+str(newname[0:-1])+" root@"+str(a)+":/erase/")
        os.remove(str(newname[0:-1]))



