import psutil

# 获取网络 IO 信息
net_io = psutil.net_io_counters()
print('net io :', net_io)
# 获取每个网络接口的 io 信息
net_io2 = psutil.net_io_counters(pernic=True)
print('every io:', net_io2)
