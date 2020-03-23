import datetime

import psutil

# 获取当前用户信息
user = psutil.users()
print('now logined user info :', user)
# 获取开机时间，并格式化
startTime = psutil.boot_time()
print('boot time is :', startTime)
startTime = datetime.datetime.fromtimestamp(startTime).strftime("%Y-%m-%d")
print('format boot time is :', startTime)
