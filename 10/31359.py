from ipaddress import *

net = ip_network(f'154.141.198.190/255.255.192.0', 0)

print(net.broadcast_address) # широковещательного адреса сети