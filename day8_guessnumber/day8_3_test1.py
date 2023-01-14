# 测验一
# 准备了三段程式码，需要你告诉我这三段程式码执行之后会产生什麽样的结果


# 1.我猜会报错
'''
def fun1(a, b):
    c = a + b
    return c

fun1(10, 20)
print(c)
'''
# 答对了 因为c是fun1里面的 在外面直接打印是没有c的值的


# 2.我猜是5
'''
x = 5
def fun2():
    x = 58
    return x

fun2()
print(x)
'''
# 答对啦 因为执行的时候返回了58 但有重新打印了x = 5 而不是x = fun2() print(x)


# 3.我猜是50
'''
x = 10
def fun3():
    global x
    x = 50
    if 2 > 1:
        x = 100
    return x
    
fun3()
print(x)
'''
# 答错了 因为只要是生命过一次的全局变量 之后在函数中就一直会是全局变量

