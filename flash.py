from mininet.net import Mininet
from network_topology import NetworkTopo
from mininet.node import Controller, RemoteController,OVSSwitch
from mininet.cli import CLI
from mininet.nodelib import NAT
from add_routes import add_routes

import threading
import time
import random

hostids = list()
hostlist = list()
atlist = list()

c0 = RemoteController( 'c0', ip = '127.0.0.1', port = 6653 )
c1 = RemoteController( 'c1', ip = '127.0.0.1', port = 6633 )

cmap = { 's0': c0, 's1': c0, 's2': c0, 's3': c0, 
         's4': c0, 's5': c1, 's6': c0, 's7': c0, 
         's8': c0, 's9': c0, 's10': c0, 
         's11':  c0, 's12': c0 }

class MultiSwitch( OVSSwitch ):
    
    def start( self, controllers ):
        return OVSSwitch.start( self, [ cmap[ self.name ] ] )     

network = NetworkTopo()
net = Mininet(topo = NetworkTopo(), switch = MultiSwitch, build = False)

for c in [c0, c1]:
        net.addController(c)



net.build()

net.start()


add_routes(net)
def getXterm(): 
        guard = net.hosts[51]
        guard.cmd('xterm')

def normalTraffic(host):
        print('Thread : ', threading.get_ident(), ' Host : ', host, ' starting normal traffic')
        host.cmd('timeout 60s hping3 -1 -i u3000 45.24.1.10')
        host.cmd('killall hping3')

def fasterTraffic(host):
        print('Thread : ', threading.get_ident(), ' Host : ', host, ' starting normal traffic')
        host.cmd('timeout 60s hping3 -1 -i u1000 45.24.1.10')
        host.cmd('killall hping3')

hostlist = [net.hosts[10], net.hosts[20], net.hosts[30], net.hosts[60],
         net.hosts[75], net.hosts[80], net.hosts[111], net.hosts[112],
         net.hosts[113], net.hosts[21], net.hosts[115], net.hosts[116],
         net.hosts[56], net.hosts[67], net.hosts[76], net.hosts[26],
         net.hosts[27], net.hosts[18], net.hosts[19], net.hosts[69],
         net.hosts[62], net.hosts[28], net.hosts[35], net.hosts[36],
         net.hosts[26], net.hosts[5], net.hosts[6], net.hosts[7]]

fhostlist = [net.hosts[11], net.hosts[21], net.hosts[31], net.hosts[59],
         net.hosts[73], net.hosts[79], net.hosts[120], net.hosts[117],
         net.hosts[119], net.hosts[118], net.hosts[22], net.hosts[105],
         net.hosts[57], net.hosts[68], net.hosts[77], net.hosts[12],
         net.hosts[22], net.hosts[33], net.hosts[55], net.hosts[61],
         net.hosts[77], net.hosts[17], net.hosts[23], net.hosts[14],
         net.hosts[29], net.hosts[12], net.hosts[13], net.hosts[75],
         net.hosts[32], net.hosts[33], net.hosts[34], net.hosts[2],
         net.hosts[3], net.hosts[4]]

xtermThread = threading.Thread(target = getXterm, args = ())
xtermThread.start()

for i in hostlist:
        atlist.append(threading.Thread(target = normalTraffic, args = (i,)))
        atlist[-1].start()

for i in fhostlist:
        atlist.append(threading.Thread(target = fasterTraffic, args = (i,)))
        atlist[-1].start()

for i in atlist:
        i.join()

xtermThread.join()

net.stop()