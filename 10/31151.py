from ipaddress import *
net = ip_network(f'185.249.55.138/255.255.192.0', 0)

print(net.broadcast_address)