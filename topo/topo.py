"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        H1 = self.addHost( 'h1' )
        H2 = self.addHost( 'h2' )
	H3 = self.addHost( 'h3' )
	H4 = self.addHost( 'h4' )
        H5 = self.addHost( 'h5' )
        H6 = self.addHost( 'h6' )

        S1 = self.addSwitch( 's1' )
        S2 = self.addSwitch( 's2' )
	S3 = self.addSwitch( 's3' )
        S4 = self.addSwitch( 's4' )
        S5 = self.addSwitch( 's5' )


        # Add links
        self.addLink( H1, S1 )
        self.addLink( H2, S1 )
        self.addLink( H3, S1 )
        self.addLink( S1, S2 )
        self.addLink( S1, S3 )
        self.addLink( S1, S4 )
        self.addLink( S2, S5 )
        self.addLink( S3, S5 )
        self.addLink( S4, S5 )
        self.addLink( S5, H4 )
        self.addLink( S5, H5 )
        self.addLink( S5, H6 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
