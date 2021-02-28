#!/usr/bin/env python

import sys
import time
from scapy.all import sendp, ARP, Ether

e = Ether()
arp = ARP(pdst='192.168.1.140')

p = e/arp

p.display()

sendp(p)
