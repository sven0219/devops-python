import dns.resolver

domain = input('Please input an domain: ')  # 输入域名地址
MX = dns.resolver.query(domain, 'MX')  # 指定查询类型为 MX# 记录
for i in MX:
    print('MX preference =',i.preference,'mail exchanger=',i.exchange)
