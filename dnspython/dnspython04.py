import dns.resolver

domain = input('Please input an domain: ')  # 输入域名地址
CNAME = dns.resolver.query(domain, 'CNAME')  # 指定查询类型为 CNAME 记录
for i in CNAME.response.answer:
    for j in i.items:
        print(j.to_text)