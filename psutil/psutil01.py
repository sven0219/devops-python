import psutil

# 获取 cpu 完整信息，需要显示所有逻辑 cpu 信息
cpu_time = psutil.cpu_times()
print("cpu_time is:", cpu_time)
# 获取单项数据信息，如用户的 CPU 时间比
cpu_user = psutil.cpu_times().user
print("cpu_user is:", cpu_user)
# 获取 CPU 的逻辑个数,默认 logical=True
cpu_count = psutil.cpu_count()
print("count is :", cpu_count)
# 获取 CPU 的物理个数，logical=False
cpu_count2 = psutil.cpu_count(logical=False)
print("count2 is :", cpu_count2)
