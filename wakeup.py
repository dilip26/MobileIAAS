# designed by dilip

import os


files=os.listdir('/erase/.')
print 'waiting'
print len(files)
while(len(files)==0):
    files = os.listdir('/erase')

tokens=files[0].split('+')
i=1

# while len(tokens)-1:
#     newname+=tokens[i]+'-\>'
#     i+=1
#
# newname=newname[0:-3]
# files[0]=files[0].replace('->','-\>')
if len(tokens)==2:
    print 'renaming '+files[0]+' with '+tokens[1]
    os.popen('mv /erase/'+files[0]+' /erase/'+tokens[1])
    os.popen('mv /erase/* /storage/')
else:
    f=0
    newname = ''
    myMAC=''
    print 'forward'
    for i in tokens:
        if f!=0:
            print i
            newname+=i+'+'
        else:
            myMAC=i;

        f=1
    newname=newname[0:-1]
    print  newname

   # os.rename(files[0], tokens[1])

#os.system('rm /erase/\\'+files[0])
