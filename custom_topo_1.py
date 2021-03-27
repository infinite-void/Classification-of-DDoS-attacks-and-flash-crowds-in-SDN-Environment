#!/usr/bin/env python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

from mininet.node import RemoteController
from mininet.node import CPULimitedHost

class LinuxRouter( Node ):

    # pylint: disable=arguments-differ
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):

    def build( self, **_opts ):
        
        r0 = self.addNode( 'r0', cls = LinuxRouter, ip = '24.10.0.1/24' )
        r1 = self.addNode( 'r1', cls = LinuxRouter, ip = '24.10.0.2/24' )
        r2 = self.addNode( 'r2', cls = LinuxRouter, ip = '36.145.0.1/24' )
        r3 = self.addNode( 'r3', cls = LinuxRouter, ip = '48.71.0.1/24' )
        r4 = self.addNode( 'r4', cls = LinuxRouter, ip = '60.2.0.1/24')

        self.addLink( r0, r1, intfName1 = 'r0-eth3', intfName2 = 'r1-eth2', 
                            params1 = { 'ip': '24.10.0.1/24' }, params2 = { 'ip' : '24.10.0.2/24' } )
        self.addLink( r1, r2, intfName1 = 'r1-eth3', intfName2 = 'r2-eth3',
                            params1 = { 'ip': '36.145.0.2/24' }, params2 = { 'ip' : '36.145.0.1/24' })
        self.addLink( r1, r3, intfName1 = 'r1-eth4', intfName2 = 'r3-eth2',
                            params1 = { 'ip': '48.71.0.2/24' }, params2 = { 'ip': '48.71.0.1/24' })
        self.addLink( r3, r4, intfName1 = 'r3-eth3', intfName2 = 'r4-eth3',
                            params1 = { 'ip': '60.2.0.2/24' }, params2 = { 'ip': '60.2.0.1/24' })

        #building R0 
        s0 = self.addSwitch('s0')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink( s0, r0, intfName2 = 'r0-eth0', params2 = { 'ip' : '3.16.1.1/24' } )  
        self.addLink( s1, r0, intfName2 = 'r0-eth1', params2 = { 'ip' : '7.31.1.1/24' } )
        self.addLink( s2, r0, intfName2 = 'r0-eth2', params2 = { 'ip' : '72.168.1.1/24' } )

        h0 = self.addHost( 'h0', ip = '3.16.1.10/24', defaultRoute = 'via 3.16.1.1' )
        h1 = self.addHost( 'h1', ip = '3.16.1.11/24', defaultRoute = 'via 3.16.1.1' )
        h2 = self.addHost( 'h2', ip = '3.16.1.12/24', defaultRoute = 'via 3.16.1.1' )
        h3 = self.addHost( 'h3', ip = '3.16.1.13/24', defaultRoute = 'via 3.16.1.1' )
        h4 = self.addHost( 'h4', ip = '3.16.1.14/24', defaultRoute = 'via 3.16.1.1' )
        h5 = self.addHost( 'h5', ip = '3.16.1.15/24', defaultRoute = 'via 3.16.1.1' )
        h6 = self.addHost( 'h6', ip = '3.16.1.16/24', defaultRoute = 'via 3.16.1.1' )
        h7 = self.addHost( 'h7', ip = '3.16.1.17/24', defaultRoute = 'via 3.16.1.1' )
        h8 = self.addHost( 'h8', ip = '3.16.1.18/24', defaultRoute = 'via 3.16.1.1' )
        h9 = self.addHost( 'h9', ip = '3.16.1.19/24', defaultRoute = 'via 3.16.1.1' )
        
        for i in range(0, 10):
            self.addLink( 'h' + str(i), s0 )

        h10 = self.addHost( 'h10', ip = '7.31.1.10/24', defaultRoute = 'via 7.31.1.1' )
        h11 = self.addHost( 'h11', ip = '7.31.1.11/24', defaultRoute = 'via 7.31.1.1' )
        h12 = self.addHost( 'h12', ip = '7.31.1.12/24', defaultRoute = 'via 7.31.1.1' )
        h13 = self.addHost( 'h13', ip = '7.31.1.13/24', defaultRoute = 'via 7.31.1.1' )
        h14 = self.addHost( 'h14', ip = '7.31.1.14/24', defaultRoute = 'via 7.31.1.1' )
        h15 = self.addHost( 'h15', ip = '7.31.1.15/24', defaultRoute = 'via 7.31.1.1' )
        h16 = self.addHost( 'h16', ip = '7.31.1.16/24', defaultRoute = 'via 7.31.1.1' )
        h17 = self.addHost( 'h17', ip = '7.31.1.17/24', defaultRoute = 'via 7.31.1.1' )
        h18 = self.addHost( 'h18', ip = '7.31.1.18/24', defaultRoute = 'via 7.31.1.1' )
        h19 = self.addHost( 'h19', ip = '7.31.1.19/24', defaultRoute = 'via 7.31.1.1' )

        for i in range(10, 20):
            self.addLink( 'h' + str(i), s1 )

        h20 = self.addHost( 'h20', ip = '72.168.1.10/24', defaultRoute = 'via 72.168.1.1' )
        h21 = self.addHost( 'h21', ip = '72.168.1.11/24', defaultRoute = 'via 72.168.1.1' )
        h22 = self.addHost( 'h22', ip = '72.168.1.12/24', defaultRoute = 'via 72.168.1.1' )
        h23 = self.addHost( 'h23', ip = '72.168.1.13/24', defaultRoute = 'via 72.168.1.1' )
        h24 = self.addHost( 'h24', ip = '72.168.1.14/24', defaultRoute = 'via 72.168.1.1' )
        h25 = self.addHost( 'h25', ip = '72.168.1.15/24', defaultRoute = 'via 72.168.1.1' )
        h26 = self.addHost( 'h26', ip = '72.168.1.16/24', defaultRoute = 'via 72.168.1.1' )
        h27 = self.addHost( 'h27', ip = '72.168.1.17/24', defaultRoute = 'via 72.168.1.1' )
        h28 = self.addHost( 'h28', ip = '72.168.1.18/24', defaultRoute = 'via 72.168.1.1' )
        h29 = self.addHost( 'h29', ip = '72.168.1.19/24', defaultRoute = 'via 72.168.1.1' )

        for i in range(20, 30):
            self.addLink( 'h' + str(i), s2 )

        
        #building r1
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        self.addLink( s3, r1, intfName2 = 'r1-eth0', params2 = { 'ip' : '18.34.1.1/24' } )
        self.addLink( s4, r1, intfName2 = 'r1-eth1', params2 = { 'ip' : '157.24.1.1/24' } )

        h30 = self.addHost( 'h30', ip = '18.34.1.10/24', defaultRoute = 'via 18.34.1.1' )
        h31 = self.addHost( 'h31', ip = '18.34.1.11/24', defaultRoute = 'via 18.34.1.1' )
        h32 = self.addHost( 'h32', ip = '18.34.1.12/24', defaultRoute = 'via 18.34.1.1' )
        h33 = self.addHost( 'h33', ip = '18.34.1.13/24', defaultRoute = 'via 18.34.1.1' )
        h34 = self.addHost( 'h34', ip = '18.34.1.14/24', defaultRoute = 'via 18.34.1.1' )
        h35 = self.addHost( 'h35', ip = '18.34.1.15/24', defaultRoute = 'via 18.34.1.1' )
        h36 = self.addHost( 'h36', ip = '18.34.1.16/24', defaultRoute = 'via 18.34.1.1' )
        h37 = self.addHost( 'h37', ip = '18.34.1.17/24', defaultRoute = 'via 18.34.1.1' )
        h38 = self.addHost( 'h38', ip = '18.34.1.18/24', defaultRoute = 'via 18.34.1.1' )
        h39 = self.addHost( 'h39', ip = '18.34.1.19/24', defaultRoute = 'via 18.34.1.1' )

        for i in range(30, 40):
            self.addLink( 'h' + str(i), s3 )

        h40 = self.addHost( 'h40', ip = '157.24.1.10/24', defaultRoute = 'via 157.24.1.1' )
        h41 = self.addHost( 'h41', ip = '157.24.1.11/24', defaultRoute = 'via 157.24.1.1' )
        h42 = self.addHost( 'h42', ip = '157.24.1.12/24', defaultRoute = 'via 157.24.1.1' )
        h43 = self.addHost( 'h43', ip = '157.24.1.13/24', defaultRoute = 'via 157.24.1.1' )
        h44 = self.addHost( 'h44', ip = '157.24.1.14/24', defaultRoute = 'via 157.24.1.1' )
        h45 = self.addHost( 'h45', ip = '157.24.1.15/24', defaultRoute = 'via 157.24.1.1' )
        h46 = self.addHost( 'h46', ip = '157.24.1.16/24', defaultRoute = 'via 157.24.1.1' )
        h47 = self.addHost( 'h47', ip = '157.24.1.17/24', defaultRoute = 'via 157.24.1.1' )
        h48 = self.addHost( 'h48', ip = '157.24.1.18/24', defaultRoute = 'via 157.24.1.1' )
        h49 = self.addHost( 'h49', ip = '157.24.1.19/24', defaultRoute = 'via 157.24.1.1' )

        for i in range(40, 50):
            self.addLink( 'h' + str(i), s4 )

        #building R2
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')

        self.addLink( s5, r2, intfName2 = 'r2-eth0', params2 = { 'ip' : '45.24.1.1/24' })
        self.addLink( s6, r2, intfName2 = 'r2-eth1', params2 = { 'ip' : '18.36.1.1/24' })
        self.addLink( s7, r2, intfName2 = 'r2-eth2', params2 = { 'ip' : '82.66.1.1/24' })

        h50 = self.addHost( 'h50', ip = '45.24.1.10/24', defaultRoute = 'via 45.24.1.1' )

        self.addLink( h50, s5)

        h51 = self.addHost( 'h51', ip = '18.36.1.11/24', defaultRoute = 'via 18.36.1.1' )
        h52 = self.addHost( 'h52', ip = '18.36.1.12/24', defaultRoute = 'via 18.36.1.1' )
        h53 = self.addHost( 'h53', ip = '18.36.1.13/24', defaultRoute = 'via 18.36.1.1' )
        h54 = self.addHost( 'h54', ip = '18.36.1.14/24', defaultRoute = 'via 18.36.1.1' )
        h55 = self.addHost( 'h55', ip = '18.36.1.15/24', defaultRoute = 'via 18.36.1.1' )
        h56 = self.addHost( 'h56', ip = '18.36.1.16/24', defaultRoute = 'via 18.36.1.1' )
        h57 = self.addHost( 'h57', ip = '18.36.1.17/24', defaultRoute = 'via 18.36.1.1' )
        h58 = self.addHost( 'h58', ip = '18.36.1.18/24', defaultRoute = 'via 18.36.1.1' )
        h59 = self.addHost( 'h59', ip = '18.36.1.19/24', defaultRoute = 'via 18.36.1.1' )
        h60 = self.addHost( 'h60', ip = '18.36.1.20/24', defaultRoute = 'via 18.36.1.1' ) 

        for i in range(51, 61):
            self.addLink( 'h' + str(i), s6 )

        h61 = self.addHost( 'h61', ip = '82.66.1.11/24', defaultRoute = 'via 82.66.1.1' )
        h62 = self.addHost( 'h62', ip = '82.66.1.12/24', defaultRoute = 'via 82.66.1.1' )
        h63 = self.addHost( 'h63', ip = '82.66.1.13/24', defaultRoute = 'via 82.66.1.1' )
        h64 = self.addHost( 'h64', ip = '82.66.1.14/24', defaultRoute = 'via 82.66.1.1' )
        h65 = self.addHost( 'h65', ip = '82.66.1.15/24', defaultRoute = 'via 82.66.1.1' )
        h66 = self.addHost( 'h66', ip = '82.66.1.16/24', defaultRoute = 'via 82.66.1.1' )
        h67 = self.addHost( 'h67', ip = '82.66.1.17/24', defaultRoute = 'via 82.66.1.1' )
        h68 = self.addHost( 'h68', ip = '82.66.1.18/24', defaultRoute = 'via 82.66.1.1' )
        h69 = self.addHost( 'h69', ip = '82.66.1.19/24', defaultRoute = 'via 82.66.1.1' )
        h70 = self.addHost( 'h70', ip = '82.66.1.20/24', defaultRoute = 'via 82.66.1.1' )

        for i in range(61, 71):
            self.addLink( 'h' + str(i), s7 )

        #building R3
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')

        self.addLink( s8, r3, intfName2 = 'r3-eth0', params2 = { 'ip' : '124.61.1.1/24' })
        self.addLink( s9, r3, intfName2 = 'r3-eth1', params2 = { 'ip' : '135.11.1.1/24' })

        h71 = self.addHost( 'h71', ip = '124.61.1.11/24', defaultRoute = 'via 124.61.1.1' )
        h72 = self.addHost( 'h72', ip = '124.61.1.12/24', defaultRoute = 'via 124.61.1.1' )
        h73 = self.addHost( 'h73', ip = '124.61.1.13/24', defaultRoute = 'via 124.61.1.1' )
        h74 = self.addHost( 'h74', ip = '124.61.1.14/24', defaultRoute = 'via 124.61.1.1' )
        h75 = self.addHost( 'h75', ip = '124.61.1.15/24', defaultRoute = 'via 124.61.1.1' )
        h76 = self.addHost( 'h76', ip = '124.61.1.16/24', defaultRoute = 'via 124.61.1.1' )
        h77 = self.addHost( 'h77', ip = '124.61.1.17/24', defaultRoute = 'via 124.61.1.1' )
        h78 = self.addHost( 'h78', ip = '124.61.1.18/24', defaultRoute = 'via 124.61.1.1' )
        h79 = self.addHost( 'h79', ip = '124.61.1.19/24', defaultRoute = 'via 124.61.1.1' )
        h80 = self.addHost( 'h80', ip = '124.61.1.20/24', defaultRoute = 'via 124.61.1.1' )

        for i in range(71, 81):
            self.addLink('h' + str(i), s8)

        h81 = self.addHost( 'h81', ip = '135.11.1.11/24', defaultRoute = 'via 135.11.1.1' )
        h82 = self.addHost( 'h82', ip = '135.11.1.12/24', defaultRoute = 'via 135.11.1.1' )
        h83 = self.addHost( 'h83', ip = '135.11.1.13/24', defaultRoute = 'via 135.11.1.1' )
        h84 = self.addHost( 'h84', ip = '135.11.1.14/24', defaultRoute = 'via 135.11.1.1' )
        h85 = self.addHost( 'h85', ip = '135.11.1.15/24', defaultRoute = 'via 135.11.1.1' )
        h86 = self.addHost( 'h86', ip = '135.11.1.16/24', defaultRoute = 'via 135.11.1.1' )
        h87 = self.addHost( 'h87', ip = '135.11.1.17/24', defaultRoute = 'via 135.11.1.1' )
        h88 = self.addHost( 'h88', ip = '135.11.1.18/24', defaultRoute = 'via 135.11.1.1' )
        h89 = self.addHost( 'h89', ip = '135.11.1.19/24', defaultRoute = 'via 135.11.1.1' )
        h90 = self.addHost( 'h90', ip = '135.11.1.20/24', defaultRoute = 'via 135.11.1.1' )

        for i in range(81, 91):
            self.addLink('h' + str(i), s9)

        #building R4
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')

        self.addLink( s10, r4, intfName2 = 'r4-eth0', params2 = { 'ip' : '116.3.1.1/24' })
        self.addLink( s11, r4, intfName2 = 'r4-eth1', params2 = { 'ip' : '180.12.1.1/24' })
        self.addLink( s12, r4, intfName2 = 'r4-eth2', params2 = { 'ip' : '92.1.1.1/24' })

        h91 = self.addHost( 'h91', ip = '116.3.1.11/24', defaultRoute = 'via 116.3.1.1' )
        h92 = self.addHost( 'h92', ip = '116.3.1.12/24', defaultRoute = 'via 116.3.1.1' )
        h93 = self.addHost( 'h93', ip = '116.3.1.13/24', defaultRoute = 'via 116.3.1.1' )
        h94 = self.addHost( 'h94', ip = '116.3.1.14/24', defaultRoute = 'via 116.3.1.1' )
        h95 = self.addHost( 'h95', ip = '116.3.1.15/24', defaultRoute = 'via 116.3.1.1' )
        h96 = self.addHost( 'h96', ip = '116.3.1.16/24', defaultRoute = 'via 116.3.1.1' )
        h97 = self.addHost( 'h97', ip = '116.3.1.17/24', defaultRoute = 'via 116.3.1.1' )
        h98 = self.addHost( 'h98', ip = '116.3.1.18/24', defaultRoute = 'via 116.3.1.1' )
        h99 = self.addHost( 'h99', ip = '116.3.1.19/24', defaultRoute = 'via 116.3.1.1' )
        h100 = self.addHost( 'h100', ip = '116.3.1.20/24', defaultRoute = 'via 116.3.1.1' ) 

        for i in range(91, 101):
            self.addLink('h' + str(i), s10)
        
        h101 = self.addHost( 'h101', ip = '180.12.1.11/24', defaultRoute = 'via 180.12.1.1' )
        h102 = self.addHost( 'h102', ip = '180.12.1.12/24', defaultRoute = 'via 180.12.1.1' )
        h103 = self.addHost( 'h103', ip = '180.12.1.13/24', defaultRoute = 'via 180.12.1.1' )
        h104 = self.addHost( 'h104', ip = '180.12.1.14/24', defaultRoute = 'via 180.12.1.1' )
        h105 = self.addHost( 'h105', ip = '180.12.1.15/24', defaultRoute = 'via 180.12.1.1' )
        h106 = self.addHost( 'h106', ip = '180.12.1.16/24', defaultRoute = 'via 180.12.1.1' )
        h107 = self.addHost( 'h107', ip = '180.12.1.17/24', defaultRoute = 'via 180.12.1.1' )
        h108 = self.addHost( 'h108', ip = '180.12.1.18/24', defaultRoute = 'via 180.12.1.1' )
        h109 = self.addHost( 'h109', ip = '180.12.1.19/24', defaultRoute = 'via 180.12.1.1' )
        h110 = self.addHost( 'h110', ip = '180.12.1.20/24', defaultRoute = 'via 180.12.1.1' )

        for i in range(101, 111):
            self.addLink('h' + str(i), s11)

        h111 = self.addHost( 'h111', ip = '92.1.1.11/24', defaultRoute = 'via 92.1.1.1' )
        h112 = self.addHost( 'h112', ip = '92.1.1.12/24', defaultRoute = 'via 92.1.1.1' )
        h113 = self.addHost( 'h113', ip = '92.1.1.13/24', defaultRoute = 'via 92.1.1.1' )    
        h114 = self.addHost( 'h114', ip = '92.1.1.14/24', defaultRoute = 'via 92.1.1.1' )
        h115 = self.addHost( 'h115', ip = '92.1.1.15/24', defaultRoute = 'via 92.1.1.1' )
        h116 = self.addHost( 'h116', ip = '92.1.1.16/24', defaultRoute = 'via 92.1.1.1' )
        h117 = self.addHost( 'h117', ip = '92.1.1.17/24', defaultRoute = 'via 92.1.1.1' )
        h118 = self.addHost( 'h118', ip = '92.1.1.18/24', defaultRoute = 'via 92.1.1.1' )
        h119 = self.addHost( 'h119', ip = '92.1.1.19/24', defaultRoute = 'via 92.1.1.1' )
        h120 = self.addHost( 'h120', ip = '92.1.1.20/24', defaultRoute = 'via 92.1.1.1' )

        for i in range(111, 121):
            self.addLink('h' + str(i), s12)

def run():
    c = RemoteController('c', '0.0.0.0', 6633)
    net = Mininet(topo=NetworkTopo(), host=CPULimitedHost, controller=None)
    net.addController(c)
    net.start()

    CLI(net)
    net.stop()

# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()