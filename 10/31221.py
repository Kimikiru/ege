from ipaddress import *

net = ip_network(f'64.237.228.143/255.255.248.0', 0)

print(net.network_address)