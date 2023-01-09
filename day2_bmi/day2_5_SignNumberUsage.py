# 运算符号、数字的用法

print(7/3)
print(7//3)         # // 是整数除法 余数部分去掉

print(7*3)
print(7**3)         # ** 次方

print(7%3)          # % 取余数

print(6+(3-7)*3)    # 存在括号的用法


'''
符号的运算优先顺序
()
** //
* / %
+ -
'''



# 四舍五入 round(目的值,四舍五入到第几位)
print(round(1.32546,2))

# 缩写  a+=1  a=a+1
num = 10
num+=1
print(num)
num*=2
print(num)