import dns.resolver

domain = input('Please input an domain: ')  # 输入域名地址
NS = dns.resolver.query(domain, 'NS')  # 指定查询类型为 NS 记录
for i in NS.response.answer:
    for j in i.items:
        print(j.to_text)