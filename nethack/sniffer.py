#!/usr/bin/env python

import sys
import getopt
import pcapy
from impacket.ImpactDecoder import EthDecoder

dev = "en0"
filter = "arp"

decoder = EthDecoder()

def handle_packet(hdr, data) :
    print (decoder.decode(data))

def usage() :
    print (sys.argv[0] + " -i <dev> -f <pcap_filter>")
    sys.exit(1)

try :
    cmd_opts = "f:i:"
    opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
    usage()


for opt in opts :
    if opt[0] == "-f" :
        filter = opt[1]
    elif opt[0] == "-i" :
        dev = opt[1]
    else :
        usage()

pcap = pcapy.open_live(dev, 1500, 1, 100)
print (f"-{filter}-")
pcap.setfilter(filter)
pcap.loop(0, handle_packet)
