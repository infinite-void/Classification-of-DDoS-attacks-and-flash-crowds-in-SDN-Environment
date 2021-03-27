from datetime import datetime

from mininet.net import Mininet
from custom_topo_1 import NetworkTopo
from mininet.node import Controller, RemoteController,OVSSwitch

network = NetworkTopo()
net = Mininet(topo=network, controller=RemoteController, switch=OVSSwitch)
net.start()

host1 = net.hosts[0]
now = datetime.now().time()
print(now)
host1.cmd('hping3 --flood 7.168.1.10')
now = datetime.now().time()
print(now)
net.stop()