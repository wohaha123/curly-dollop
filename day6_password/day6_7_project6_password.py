# 密码产生器
# random.shuffle()打乱列表元素顺序。
# join凑在一起

import random
up_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
low_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
mark_list = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

# 需要：抽取n个；在list里抽；list里共k个值; element是list里面的单个一一值
lottery_list = []
def lottery():
    i = 0
    while i < n:
        lottery_list.append(list[random.randint(0, k - 1)])
        i += 1
# lottery_elements =

print("欢迎使用密码产生器~")

up = int(input("请问需要几个大写英文字母？"))
n = up
list = up_list
k = len(list)
lottery()

low = int(input("请问需要几个小写英文字母？"))
n = low
list = low_list
k = len(list)
lottery()

number = int(input("请问需要几个数字？"))
n = number
list = number_list
k = len(list)
lottery()

mark = int(input("请问需要几个符号？"))
n = mark
list = mark_list
k = len(list)
lottery()

random.shuffle(lottery_list)
print(''.join(lottery_list))



'''
1.随机抽取n个xx（可重复）
2.将抽取的所有在随机排序
'''

