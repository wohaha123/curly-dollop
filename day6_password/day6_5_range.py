# range() 函数
# 可以让for循环跑过一连串的整数

# 产生 1 <= i < 11 的整数
for i in range(1, 11):
    print(i)

# 产生 1 <= j < 10 的整数，数字间隔3
for j in range(1, 10, 3):
    print(j)

# 计算1+2+3+...+50
k = 0
for l in range(1, 50):
    k += l
print(f"总和为{k}")