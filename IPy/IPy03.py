from IPy import IP

# 接受用户输入的 IP 地址或网段地址
ip_s = input('Please input an IP or net-range:')
ips = IP(ip_s)
# 如果长度大于 1 那就是一个网段地址
if len(ips) > 1:
    print('net:', ips.net())  # 输出网络地址
    print('netmask:', ips.netmask())  # 输出网络掩码地址
    print('broadcast:', ips.broadcast())  # 输出网络广播地址
    print('reverse address:', ips.reverseName()[0])  # 输出地址反向解析
    print('subnet:', len(ips))  # 输出网络子网数
else:
    print('reverse address:', ips.reverseName()[0])  # 输出地址反向解析

print('hexadecimal:', ips.strHex())  # 输出十六进制地址
print('binary ip', ips.strBin())  # 输出二进制地址
print('ipType:', ips.iptype())  # 输出地址类型
