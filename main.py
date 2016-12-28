import os
import  time
ls = os.listdir("/home/akshay/erase/")
while (len(ls) == 0):
    ls = os.listdir("/home/akshay/erase/")
time.sleep(1)
fname = ls.pop()

ch = open("/home/akshay/erase/" + fname, "r")
fs = open("/home/akshay/myclients.txt", "a")
r = int(ch.read())
print r
if r == 1:
    x = os.popen('create_ap --list-client ap0')
    f = x.read();

    list = f.split('\n')
    f = 0
    for i in list:
        if f != 0 and f < (len(list) - 1):
            ls = i.split()
            fs.write(ls[1] + " " + ls[0])
            print ls[1] + " " + ls[0]
        f += 1
    time.sleep(5)
    os.popen("scp /home/akshay/myclients.txt cool@192.168.12.206:/home/cool/child/")
    print "sentss"
    time.sleep(3)
    os.remove("/home/akshay/myclients.txt")
    os.remove("/home/akshay/erase/"+fname)
else:
    print "kuchh toh baki hai"



