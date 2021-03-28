from mininet.net import Mininet
from custom_topo_1 import NetworkTopo
from mininet.node import Controller, RemoteController,OVSSwitch
from mininet.cli import CLI
from add_routes import add_routes

import threading
import time
import random

hostids = list()
hostlist = list()
atlist = list()

network = NetworkTopo()
net = Mininet(topo=network, controller=RemoteController, switch=OVSSwitch)
net.start()

add_routes(net)

def normalTraffic(host):
        print('Thread : ', threading.get_ident(), ' Host : ', host, ' starting normal traffic')
        host.cmd('timeout 60s hping3 -1 --fast 45.24.1.10')
        host.cmd('killall hping3')

while len(hostids) < 50:
        host = random.randint(0, 120)
        if host != 50 or host not in hostids:
                hostids.append(host)

for id in hostids:
        hostlist.append(net.hosts[id])

for i in hostlist:
        atlist.append(threading.Thread(target = normalTraffic, args = (i,)))
        atlist[-1].start()

for i in atlist:
        i.join()

net.stop()