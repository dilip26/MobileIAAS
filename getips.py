import os
def Get_ips(mac):
    x = os.popen('create_ap --list-client ap0')
    f = x.read()
    ls=''
    ip=''
    list = f.split('\n')
    f=0
    for i in list:
        if f != 0 and f < (len(list) - 1):
            ls = i.split()
            if(ls[0]==mac):
                ip+=ls[1]+' '
        f += 1
    return ip
print Get_ips('64:db:43:4f:1b:72')