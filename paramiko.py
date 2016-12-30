import paramiko
paramiko.util.log_to_file('/home/sourabh/paramiko.log')

# Open a transport

host = "192.168.12.142"
port = 22
transport = paramiko.Transport((host, port))

# Auth

password = "asdfghjkl;'"
username = "akshay"
transport.connect(username = username, password = password)

# Go!

sftp = paramiko.SFTPClient.from_transport(transport)

# Download

#filepath = '/etc/passwd'
#localpath = '/home/remotepasswd'
#sftp.get(filepath, localpath)

# Upload

filepath = '/home/akshay/erase/list_clients.py'
localpath = '/home/sourabh/DilipPro/MobileIAAS/list_clients.py'
sftp.put(localpath, filepath)

# Close

sftp.close()
transport.close()
