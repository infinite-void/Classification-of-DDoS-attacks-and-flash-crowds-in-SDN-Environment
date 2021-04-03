from mininet.net import Mininet
from custom_topo_1 import NetworkTopo
from mininet.node import Controller, RemoteController,OVSSwitch
from mininet.cli import CLI
from add_routes import add_routes
import threading
import time

network = NetworkTopo()
net = Mininet(topo=network, controller=RemoteController, switch=OVSSwitch)
net.start()
add_routes(net)

def attackTraffic(host):
        print(host, ' starting attack')
        host.cmd('timeout 60s hping3 -1 --flood --rand-source 45.24.1.10')
        host.cmd('killall hping3')

def normalTraffic(host):
        print(host, ' starting normal traffic')
        host.cmd('timeout 60s hping3 -1 --faster 45.24.1.10')
        host.cmd('killall hping3')

hlist = [net.hosts[10], net.hosts[20], net.hosts[30], net.hosts[60],
         net.hosts[75], net.hosts[80], net.hosts[111], net.hosts[112],
         net.hosts[113], net.hosts[114], net.hosts[115], net.hosts[116],
         net.hosts[56], net.hosts[67], net.hosts[76]]
                
bhlist = [net.hosts[15], net.hosts[25], net.hosts[35], net.hosts[45],
        net.hosts[55], net.hosts[65], net.hosts[66], net.hosts[77],
        net.hosts[87], net.hosts[97], net.hosts[98], net.hosts[100],
        net.hosts[91], net.hosts[26], net.hosts[29], net.hosts[32],
        net.hosts[36], net.hosts[46], net.hosts[47], net.hosts[48],
        net.hosts[81], net.hosts[82], net.hosts[83], net.hosts[84],
        net.hosts[21], net.hosts[22], net.hosts[23], net.hosts[24],
        net.hosts[0], net.hosts[1], net.hosts[2], net.hosts[3],
        net.hosts[4], net.hosts[5], net.hosts[6], net.hosts[7],
        net.hosts[8], net.hosts[9], net.hosts[11], net.hosts[12]]

time.sleep(5)

atlist = []
for i in hlist:
        atlist.append(threading.Thread(target=attackTraffic, args=(i,)))
        atlist[-1].start()
for i in bhlist:
        atlist.append(threading.Thread(target=normalTraffic, args=(i,)))
        atlist[-1].start()

for i in atlist:
        i.join()



net.stop()