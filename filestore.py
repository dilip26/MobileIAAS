import os
fp=open("Paths.txt","r")
data=fp.read().split('\n')
var1=0
for i in data:
    os.rename("xyz.txt.p_"+str(var1),str(i)+"->xyz.txt.p_"+str(var1))
    print "xyz.txt.p_"+str(var1),str(i)+"->xyz.txt.p_"+str(var1)
    print str(i)
    var1 += 1
