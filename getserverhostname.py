import os

host=os.popen("hostname -I|awk '{print $1}'")
thost=host.read()
host=thost.split('.')
host=host[0:-1]
server_host=""
for i in host:
    server_host+=i+'.'
server_host+='1'
print  server_host

`