from ipaddress import ip_network #обязательный импорт

net = ip_network(f'192.168.159.86/255.255.252.0', 0) # находим адрес сети по ардесу улза и маске сети

print(net.network_address) # выводим адрес сети