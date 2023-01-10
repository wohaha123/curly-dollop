# 关于将列表连接成字串

list = ['你', '好', '我', '是', '小', '白']

# 初阶版
new_str1 = ""
for char in list:
    new_str1 += char
print(new_str1)

# 高阶版 join
new_str2 = "".join(list)            # 引号中是两字串之间分割的东西
print(new_str2)

new_str3 = "\\".join(list)
print(new_str3)


