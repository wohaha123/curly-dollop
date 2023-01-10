# 测试2 今晚吃什么 (进阶版)
# 分割split
# 统计len

print("欢迎使用今晚吃什么~")
food = input("请输入晚餐选项（中间请用,隔开）\n")
food_list = food.split(",")                     # split 分割 的用法
food_len = len(food_list)                       # len 长度 的用法

import random
num = random.randint(0, food_len-1)

print(f"今晚吃{food_list[num]}")
