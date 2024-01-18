#!/usr/bin/env python

"""
Creating a Mininet object
Add nodes to it
Base configuration: two hosts and one switch
"""

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import setLogLevel, info

def baseNet():

    "Create a network and add nodes to it."

    net = Mininet( controller=Controller, link=TCLink, waitConnected=True )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
    h3 = net.addHost( 'h3', ip='10.0.0.3' )
    h4 = net.addHost( 'h4', ip='10.0.0.4' )
    h5 = net.addHost( 'h5', ip='10.0.0.5' )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )

    info( '*** Creating links\n' )
    net.addLink( h1, s1, bw=30, delay='0ms', loss=0, use_htb=True )
    net.addLink( h2, s1, bw=30, delay='5ms', loss=0, use_htb=True )
    net.addLink( h3, s1, bw=5, delay='5ms', loss=0, use_htb=True )
    net.addLink( h4, s1, bw=5, delay='50ms', loss=5, use_htb=True )
    net.addLink( h5, s1, bw=5, delay='5ms', loss=10, use_htb=True )

    info( '*** Starting network\n')
    net.start()
    print("Host", h1.name, "has IP adress", h1.IP(), "and MAC adress", h1.MAC())
    print("Host", h2.name, "has IP adress", h2.IP(), "and MAC adress", h2.MAC())
    print("Host", h3.name, "has IP adress", h3.IP(), "and MAC adress", h3.MAC())
    print("Host", h4.name, "has IP adress", h4.IP(), "and MAC adress", h4.MAC())
    print("Host", h5.name, "has IP adress", h5.IP(), "and MAC adress", h5.MAC())

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    baseNet()
