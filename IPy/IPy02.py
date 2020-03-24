from IPy import IP

print(IP('192.168.1.0').make_net('255.255.255.0'))
print(IP('192.168.1.0/255.255.255.0', make_net=True))
print(IP('192.168.1.0-192.168.1.255', make_net=True))
