# A simple and lively wait program that supports multiple time formats for convenience
# Displaying a countdown with a decreasing number in the console
# It's in python, allowing it can be used in all consoles
#
# Written by Wei Hua
# weihuathu@gmail.com, 2024-06

import datetime
import sys
import time

# 定义支持的时间格式(Supported time format)
# :%H   Hour in 24 (0~23) format
# :%M   Minutes in this hour (if applicable) or next hour 
# 示例(Examples)
# Assumming the current time is 2024-06-16 15:18:00
# param                     target_time
# 13                        13:00 the next day
# 16                        16:00
# :10                       16:10
# :30                       15:30
# 2024-06-30 15             2024-06-30 15:00:00   
supported_formats = ['%H:%M:%S', '%H:%M', '%H', ':%M', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d %H', '%Y-%m-%d']

# 获取传入的时间参数
if len(sys.argv) < 2:
    print("Param: time point to wait.\nSupported format : %s" % ', '.join(supported_formats))
    sys.exit(1)

time_str = ' '.join(sys.argv[1:])

# 尝试用支持的格式解析时间字符串
target_time = None
for fmt in supported_formats:
    try:
        target_time = datetime.datetime.strptime(time_str, fmt)
        break
    except ValueError:
        pass

# 检查是否能成功解析时间字符串
if target_time is None:
    print("Can not parse the time string!\nSupported format : %s" % ', '.join(supported_formats))
    sys.exit(1)
#print(target_time)

now = datetime.datetime.now()
if target_time.date() < now.date():
    # 如果是分钟，则表示到下一个小时的指定分钟
    # :%M   minutes in this hour (if applicable) or next hour 
    if fmt == ':%M':
        minute_target   = target_time.minute
        if now.minute < target_time.minute:
            target_time = now.replace(minute=minute_target, second=0, microsecond=0)
        else:
            target_time = (now + datetime.timedelta(hours=1)).replace(minute=minute_target, second=0, microsecond=0)
    else:
        target_time = datetime.datetime.combine(now.date(), target_time.time())

if target_time < now:
    target_time += datetime.timedelta(days=1)

print("[target_time] "+(target_time.strftime("%Y-%m-%d %H:%M:%S")))
while True:
    time.sleep(1)
    now = datetime.datetime.now()
    if now>=target_time:
        break;
    sec = round((target_time-now).total_seconds())
    sys.stdout.write("\r" + str(sec) + " sec to wait ...")
    sys.stdout.flush()

# prompt the start time
sys.stdout.write("\rwork start: "+(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"\n")
sys.stdout.flush()
