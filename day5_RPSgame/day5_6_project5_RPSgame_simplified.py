# 简化版
# 直接对应123 srp

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

import random

opts = ["s", "r", "p"]
user_choice = input("请输入字母 s(剪刀) r(石头) p(布)")
computer_choice = opts[random.randint(0, 2)]

print("你出：")
if user_choice == "s":
    print(scissor)
elif user_choice == "r":
    print(rock)
else:
    print(paper)

print("电脑出：")
if computer_choice == "s":
    print(scissor)
elif computer_choice == "r":
    print(rock)
else:
    print(paper)

if (user_choice == "s" and computer_choice == "p") or\
   (user_choice == "r" and computer_choice == "s") or \
   (user_choice == "p" and computer_choice == "r"):
    print("恭喜你赢了！")
elif (user_choice == "s" and computer_choice == "s") or\
     (user_choice == "r" and computer_choice == "r") or \
     (user_choice == "p" and computer_choice == "p"):
    print("平手~")
else:
    print("你输了QQ")