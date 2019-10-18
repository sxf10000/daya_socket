import os

taskinfo =os.popen("tasklist /NH /FO CSV")

task = {}
line = taskinfo.readline()

while line:
    line = line.replace('"','')
    alist = line.split(",")
    task[alist[1]] = alist[0]
    line=taskinfo.readline()
taskinfo.close()
netinfo= os.popen("netstat -naO")

line = netinfo.readline()
line = netinfo.readline()
line = netinfo.readline()
line = netinfo.readline()
line = netinfo.readline()

alist = ["Proto","Local Address","Foreign Address","State","PID","Progrem name"]

print("%-8s%-25s%-25s%-15s%-8s\t%-s"%(alist[0],alist[1],alist[2],
                                        alist[3],alist[4],alist[5]))
while line:
    alist= line.split()
    if len(alist)==4:
        alist.append(alist[3])
        #UDP    0.0.0.0:500        *:*       1028   1028
        #UDP    0.0.0.0:500        *:*       1028   1028  EduRender.exe
        alist[3]=''
    alist.append(task[alist[-1]])
    print("%-8s%-25s%-25s%-15s%-8s\t%-s"% (alist[0], alist[1], alist[2],
                                             alist[3], alist[4], alist[5]))
    line = netinfo.readline()
netinfo.close()