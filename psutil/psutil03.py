import psutil

# 获取磁盘完整信息
disk_info = psutil.disk_partitions()
print("info:", disk_info)
# 获取分区使用情况,需要传一个 path 参数，这里我们取/路径
disk_usage = psutil.disk_usage('/')
print("usage info:", disk_usage)
# 获取磁盘总的 IO 个数、读写信息
io_counts = psutil.disk_io_counters()
print('io_counts:', io_counts)
# 获取单个分区的 IO 个数
io_counts2 = psutil.disk_io_counters(perdisk=True)
print(io_counts2)
