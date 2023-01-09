# 函数 function
# 命名规则和变量一样

def print_info(name, age, height):
    print(f"{name}今年{age}岁")
    print(f"{name}身高{height}公分")

print_info("小菊", 18, 170)
print_info(name = "小绿", height = 160, age = 30)     # 顺序写错可以赋值