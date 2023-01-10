# 列表 list
# 列表这个数据类型可以

score1 = 80
score2 = 60
score3 = 56
score4 = 89
score5 = 78
score6 = 80     # 这样一个个输入缺乏效率

# 创建了一个列表 里面有3个数据，分别是整数80 60 56 89 78
scores = [80, 60, 56, 89, 78, 80]
print(scores)
print(scores[0])
print(scores[0], scores[1])     # 取得数据

# 列表里也可以写不同的数据类型
list1 = [456, "你好", True, 546.67568]
print(list1[0], list1[1], list1[2], list1[3])
print(list1[1] + "qwerty7410!")

# 在建好的列表后面新增数据  append vt. 附加；贴上；盖章 n. [计]设置数据文件的搜索路径
scores.append(70)
print(scores)

# 查找列表里的某个数据出现了几次  listname.count(obj)
count = scores.count(80)
print(count)




print("\n\n====================================================================================================\n\n")
# ====================================================================================================

# Python怎么向列表中添加多个元素：
# 学习参考：https://blog.csdn.net/m0_51713294/article/details/112389296
# Python的列表是多变灵活的数据结构，向列表中添加元素，
# 可以使用append()方法，或者extend()方法，还可使用insert()方法。
# insert() 主要用来插入元素，当向列表末尾添加元素时，还是应该使用 append() 方法

# append vt. 附加；贴上；盖章 n. [计]设置数据文件的搜索路径
# extend vt. & vi. (空间、时间等)延伸；延续 vt. 延长；扩展；达到(某一点) 尽可能地伸开(身体某部) 给予，提供，发出
# insert vt. 插入；嵌入 n. 插入物

# 可用 "+" 连接列表
name = ['qwerty7410']
address = ["sea"]
info = name + address
print(info)
print(info[0])
print("\n")


# 111111111111111111111111111111append111111111111111111111111111111
# 使用append()向列表的末尾添加元素
# 语法格式：listname.append(obj)
# 举个例子：scores.append(70)
# obj表示添加到末尾的数据，可以是单个元素、列表、元组（和列表类似 但元组创建后不可改）

# append()使用示例：

a_list = ["sasdf", 34, -56]

# 追加元素
a_list.append('3453')
print(a_list)

# 追加元组，元组被当成一个元素
a_tuple_add = (54.6, 5)
a_list.append(a_tuple_add)
a_list.append((345, 6))
# 两种追加元组的方法都可以 tuple到一起或（）到一起
print(a_list)

# 追加列表，列表被当成一个元素
a_list_add = [36, 657, 'h']
a_list.append(a_list_add)
print(a_list)

# 运行结果：
# ['sasdf', 34, -56, '3453']
# ['sasdf', 34, -56, '3453', (54.6, 5), (345, 6)]
# ['sasdf', 34, -56, '3453', (54.6, 5), (345, 6), [36, 657, 'h']]
print("\n")



# 222222222222222222222222222222extend222222222222222222222222222222
# 使用extend()添加元素
# 不将被追加的列表或元组当成一个整体，而是只追加列表中的元素
# 语法格式：listname.extent(obj)
# 举个例子：list1.extend((345, 6))

# extend()使用示例：

b_list = ["da", 32]

# 追加元组中的所有元素
b_list.extend((435, 6))
print(b_list)

# 追加列表中的所有元素
b_list.extend(['cv', 345, "56"])
print(b_list)

# 追加区间中的所有元素
b_list.extend(range(97,100))        # range(a, b) a<=x<b int
print(b_list)

# 运行结果：
# ['da', 32, 435, 6]
# ['da', 32, 435, 6, 'cv', 345, '56']
# ['da', 32, 435, 6, 'cv', 345, '56', 97, 98, 99]
print("\n")



# 333333333333333333333333333333insert333333333333333333333333333333
# 使用insert()方法插入元素
# 用于在列表中间增加元素
# 和 append() 方法一样，无论插入的对象是列表还是元组，都只会将其整体视为一个元素。
# 语法格式：listname.insert(a, obj)
# 举个例子：list1.insert(5, "345")     在索引5处插入字符串

# insert()使用示例：

c_list = list(range(1,6))
print(c_list)

# 在索引3处插入字符串
c_list.insert(3, 'afaf')
print(c_list)

# 在索引3处插入列表
c_list.insert(3, ['sfg', 356])
print(c_list)

# 运行结果：
# [1, 2, 3, 4, 5]
# [1, 2, 3, 'afaf', 4, 5]
# [1, 2, 3, ['sfg', 356], 'afaf', 4, 5]
print("\n")
