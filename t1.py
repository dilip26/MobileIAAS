import os

f=os.popen('ifconfig ap0|grep \'inet addr:\'|awk \'{print substr($2,6,length($2)-1)}\'')
host=f.read()
print host[0:-1]
