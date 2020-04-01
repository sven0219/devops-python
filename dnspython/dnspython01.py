import dns.resolver

domain = input('Please input an domain: ')  # 输入域名地址
A = dns.resolver.query(domain, 'A')  # 指定查询类型为 A 记录
for i in A.response.answer:
    for j in i.items:
        print(j.address)

