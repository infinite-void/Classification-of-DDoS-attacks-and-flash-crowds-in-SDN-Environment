import scapy
from scapy.all import *
from math import log2
import time

def shannon(boe):
    total = sum(boe.values()) 
    return sum(freq / total * log2(total / freq) for freq in boe.values())

def getTraffic(x):
        tc = dict()
        for i, j in x.items():
                subnet = '.'.join(i.split('.')[:2]) + '.0.0'
                if(tc.get(subnet)):
                        tc[subnet] += 1
                else:
                        tc[subnet] = 1
        return tc

pkt_count = dict()

def pktcount(x):
        global pkt_count
        srcip = x[IP].src
        if(pkt_count.get(srcip)):
                pkt_count[srcip] += 1
        else:
                pkt_count[srcip] = 1
        

t = AsyncSniffer(iface = "guard-eth0", prn = pktcount, filter = 'ip')

t.start()

time.sleep(30)

t.stop()

tc = getTraffic(pkt_count)

print(pkt_count)

print('Source Entropy : ', shannon(pkt_count))
print(tc)
print('TC Entropy : ', shannon(tc))
