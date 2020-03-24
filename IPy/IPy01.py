from IPy import IP

ip = IP('192.168.0.0/16')
# 输出个数
print(ip.len())
# 打印所有 ip 地址清单
for x in ip:
    print(x)