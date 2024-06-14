# Name: w
# A simple and lively wait program that supports multiple time formats for convenience
# Displaying a countdown with a decreasing number in the console
# It's in python, allowing it can be used in all consoles

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
