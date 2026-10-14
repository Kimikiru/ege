from ipaddress import ip_network

ip = '84.32.84.32'

for mask in range(33):
    bin_ip = ''
    net = ip_network(f'{ip}/{mask}', strict=False)

    maxx = net[-2]
    maxx = str(maxx).split('.')

    for i in maxx:
        bin_ip += f"{int(i):08b}"
    if bin_ip.count('1') == 19:
        print(mask, maxx)
        break