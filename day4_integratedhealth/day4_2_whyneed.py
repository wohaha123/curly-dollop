# 为什么需要函数？
# 可重复使用 可大大减少代码中重复的地方

def print_info(name, age, height, weight):
    print(f"{name}今年{age}岁")
    print(f"{name}身高{height}公分")
    print(f"{name}体重{weight}公斤")

print_info("小白", 24, 179, 70)
print_info("小黑", 10, 129, 30)
print_info("小蓝", 59, 189, 50)
print_info("小绿", 33, 189, 50)


