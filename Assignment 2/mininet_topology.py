from mininet.log import setLogLevel
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import OVSController, OVSBridge

def start_mininet():
  MCT = MininetCustomTopology()
  network = Mininet( topo = MCT, controller = OVSController, switch = OVSBridge, link = TCLink)
  network.start()
  CLI(network)
  network.stop()

class MininetCustomTopology(Topo):
  def build(self, **_kwargs):
    R1 = self.addSwitch('R1')
    R2 = self.addSwitch('R2')

    host_node_A = self.addHost('A', ip='192.0.0.0/8')
    host_node_B = self.addHost('B', ip='192.0.0.1/8')
    host_node_C = self.addHost('C', ip='192.0.0.2/8')
    host_node_D = self.addHost('D', ip='192.0.0.3/8')

    self.addLink(host_node_A, R1, bw = 1000, delay = '1ms', loss = 0)
    self.addLink(R1, R2, bw = 500, delay = '10ms', loss = 0)
    self.addLink(R2, host_node_B, bw = 1000, delay = '1ms', loss = 0)
    self.addLink(host_node_D, R1, bw = 1000, delay = '1ms', loss = 0)
    self.addLink(R2, host_node_C, bw = 1000, delay = '5ms', loss = 0)

if __name__ == '__main__':
  setLogLevel( 'info' )
  start_mininet()