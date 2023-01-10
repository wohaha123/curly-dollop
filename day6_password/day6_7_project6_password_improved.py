# 密码产生器 改良版 简化版

# for i in range(0, 3):
# 即进入循环3次的意思
# 该语句可以控制进入循环的次数

# password = ""
# 之后直接把东西放在该字串中了

import random
up_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
low_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
mark_list = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

print("欢迎使用密码产生器~")
up = int(input("请问需要几个大写英文字母？"))
low = int(input("请问需要几个小写英文字母？"))
number = int(input("请问需要几个数字？"))
mark = int(input("请问需要几个符号？"))

password = ""
for i in range(0, up):
    password += up_list[random.randint(0, 25)]
for i in range(0, low):
    password += low_list[random.randint(0, 25)]
for i in range(0, number):
    password += number_list[random.randint(0, 9)]
for i in range(0, mark):
    password += mark_list[random.randint(0, 9)]

password_list = list(password)
random.shuffle(password_list)
print(''.join(password_list))



# random.shuffle(lottery_list)
# print(''.join(password_list))




