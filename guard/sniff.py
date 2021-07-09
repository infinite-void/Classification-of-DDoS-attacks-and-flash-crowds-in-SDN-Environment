import scapy
from scapy.all import *
from math import log2
import time
import numpy as np
import pandas as pd

dataset = pd.read_csv('Simulated_Traffic_Data.csv')
X = dataset.iloc[:,[0,2]].values
y = dataset.iloc[:,2].values

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)


def shannon(boe):
    total = sum(boe.values()) 
    return sum(freq / total * log2(total / freq) for freq in boe.values())

def getTraffic(x):
        tc = dict()
        for i, j in x.items():
                subnet = '.'.join(i.split('.')[:2]) + '.0.0'
                if(tc.get(subnet)):
                        tc[subnet] += j
                else:
                        tc[subnet] = j
        return tc

pkt_count = dict()

def pktcount(x):
        global pkt_count
        
        srcip = x[IP].src
        if srcip == '45.24.1.10':
                return 

        if(pkt_count.get(srcip)):
                pkt_count[srcip] += 1
        else:
                pkt_count[srcip] = 1
sfile = open('sample.txt', 'w')
sfile.write('working...')
sfile.close()
while True:
        pkt_count.clear()
        t = AsyncSniffer(iface = "guard-eth0", prn = pktcount, filter = 'ip')
        t.start()
        time.sleep(30)
        t.stop()

        tc = getTraffic(pkt_count)

        print(pkt_count)
        srcip = shannon(pkt_count)
        print('Source Entropy : ', shannon(pkt_count))
        print(tc)
        print('TC Entropy : ', shannon(tc))
        tcip = shannon(tc)
        traffic_type = classifier.predict(np.array([srcip, tcip])

