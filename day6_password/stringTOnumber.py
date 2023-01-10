# Python中将列表中的字符串转为数字
# 见 https://blog.csdn.net/Mr_FengT/article/details/90943766

# 有一个数字字符的列表
# numbers = ['1', '5', '10', '8']

# 想将其转换为
# numbers = [1, 5, 10, 8]

# 用一个循环来解决
# 建立空列表，一一取出字符，转为整数，append到空列表的后面
numbers = ['1', '5', '10', '8']
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
numbers = new_numbers
print(numbers)

# 有没有更简单的语句可以做到呢？
# 1.
numbers = ['657', '878', '6', '-5']
numbers = [int(x) for x in numbers]
print(numbers)

# 2.Python2.x可以使用map函数   (该版本不能用)
numbers = ['1', '45', '6']
numbers = map(int, numbers)
print(numbers)

# 3.Python3.x返回的是map对象，可以转换为list
numbers = ['1', '45', '6']
numbers = list(map(int, numbers))
print(numbers)

# 4.还有一种比较复杂点（怎么弄不出来呢）
'''
numbers = ['1', '55', '888', '89']
for i, v in enumerate(numbers):
    number[i] = int(v)
print(numbers)
'''




# =======================Python中的字符数字之间的转换函数====================================


# 将x转换为一个整数
# 1.int(x)
int(675)    # 675

# 2.int(x[,base])
# 进制转换的原理:https://www.zhihu.com/question/20993504
int("12", 5)    # 7
int("1265", 8)  # 693
# 把x(视为base进制)转换为十进制之下的数字


# 将x转换为一个长整数
# 1.long(x)
# 2.long(x[,base])
# Python3.x中没有长整型，所有都归为一种整数类型int，没有Python2.x中的long


# 将x转换为一个复数
# 语法：complex(real[,imag])
# 创建一个值为 real + imag * j的复数，或转化一个字符串或数为复数。 若第一个参数为字符串，则无需指定第二个参数
# 说明：
# real -- int, float, string
# imag -- int, float

complex(1, 2)      # (1+2j)
complex(1)         # (1+0j)
complex("1")       # (1+0j)
complex("1+2j")    # (1+2j) +两边有空格会报错











