from ipaddress import *

net = ip_network(f'189.163.226.71/255.255.255.240', 0)

print(net.network_address)