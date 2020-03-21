import psutil

# 使用psutil.virtual_memory()获取内存完整信息
mem = psutil.virtual_memory()
print("memory info is", mem)
# 获取内存总数
print("mem total is :", mem.total)
# 获取空闲内存数
print("mem free is :", mem.free)
# 获取 swap 分区信息
swap = psutil.swap_memory()
print("swap is :", swap)
