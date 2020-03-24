import dns.resolver
import os
import httplib2

iplist = []  # 定义域名 IP 列表变量
appdomain = 'www.baidu.com'  # 定义业务域名


def get_iplist(domain=""):  # 域名解析行数，解析成功的 ip 将被追加到 iplist
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print("dns resolver error:", str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)  # 将 ip 追加到 iplist
    return True


def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    httplib2.socket.setdefaulttimeout(5)  # 定义 http 连接超时时间，单位秒
    conn = httplib2.HTTPConnectionWithTimeout(checkurl)  # 创建连接对象

    try:
        conn.request("GET", "/", headers={"Host": appdomain})  # 发起 URL 请求，添加 host 主机头
        r = conn.getresponse()
        getcontent = r.read(15)  # 获取 URL 页面前 15 个字符
    finally:
        if "html" in str(getcontent):  # 判断是否包含 html 字符，包含说明请求成功
            print(ip + "[OK]")
        else:
            print(ip + "[ERROR]")


if __name__ == '__main__':
    if get_iplist(appdomain) and len(iplist) > 0:  # 条件：域名解析正确且至少返回一个 IP
        for ip in iplist:
            checkip(ip)
    else:
        print("dns reslover error")
