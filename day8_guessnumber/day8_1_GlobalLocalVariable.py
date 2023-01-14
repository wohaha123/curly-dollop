# 变量的作用域  全局变量 局部变量
# global, local variable


e = 10
def abc(a, b):
    c = a+b
    print(c)
abc(1, 2)     # 3


# 在函数外部无法印出c
# print(c)    # NameError: name 'c' is not defined
# 因为变量c是局部变量 是在abc()函数内部创建的 无法在函式外部进行使用


# 全局变量可以印出
print(e)


# 在函数内部可以呼叫全局变量
# 且不同函数内创建的相同变量名的变量是独立的
def efg():
    c = 10
    print(e)
efg()


# 做缩进所创建的变量都是区域变量吗？
# 实验
if True:
    a = 2
print(a)
# 可印出a 所以a并不是局部变量
# 只有在函数内部创建的才是局部变量


