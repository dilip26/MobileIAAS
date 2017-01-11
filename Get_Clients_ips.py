import os

def Ping_clients():
    x = os.popen('create_ap --list-client ap0')
    f = x.read()
    list = f.split('\n')
    f=0
    for i in list:
        if f != 0 and f < (len(list) - 1):
            ls = i.split()
            print 'pinged ' + ls[1]
            os.system('ping -c 1 '+ ls[1])
        f += 1
Ping_clients()