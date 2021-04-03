import scapy
from scapy.all import *

# a = sniff(iface="guard-eth0", count=5)

# for pkt in a:
#         print(pkt.summary())    
#         print(pkt.getlayer(IP).src)

count = 0
def pktcount(x):
        global count
        count += 1
        print(x.summary())
        

t = AsyncSniffer(iface = "guard-eth0", prn=pktcount, filter = 'ip')

t.start()

time.sleep(30)

t.stop()
print(count)