# scan open ports  to avoid security gaps || to find open ports in target mahcines [illegal]

import socket
import threading
from queue  import Queue

target='127.0.0.1'
openPorts=[]
queue=Queue()

def portScan(port):
    try: # try to connect
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET=internet socket not a unix socket , SOCK_STREAM= using TCP not UDP
        sock.connect((target,port)) # connect to the target on this port 
        return True # the port is open
    except :
        return False


# ============SimplePortCheck==============
# for port in range(1,1024):
#     result=portScan(port)
#     if result :
#         print("port {} is open!".format(port))

# we gone use queuse with threading to avoid chking the same port more then once

def fill_queue(portList):
    for port in portList:
        queue.put(port)

def worker():
    while not queue.empty():
        port=queue.get()
        if portScan(port):
            print("port {} is open!".format(port))
            openPorts.append(port)


portList=range(1,1024)
fill_queue(portList)

threadList=[]

for i in range(10):
    thread=threading.Thread(target=worker) # target =target function
    threadList.append(thread)

for i in threadList :
    i.start()
    
for i in threadList :
    thread.join() 

print(openPorts) # we want t print thisonly when all the ports are don that's why we made a join
    

