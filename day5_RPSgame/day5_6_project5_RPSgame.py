# 剪刀、石头、布 游戏
# 字串也可以用三个引号来做表示

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

start = input("请输入字母 s(剪刀) r(石头) p(布)")

if start == "s":
    print(f"你出：\n{scissor}")
elif start == "r":
    print(f"你出：\n{rock}")
elif start == "p":
    print(f"你出：\n{paper}")

import random
num = random.randint(0, 2)

if num == 0:
    print(f"电脑出：\n{scissor}")
elif num == 1:
    print(f"电脑出：\n{rock}")
elif num == 2:
    print(f"电脑出：\n{paper}")

if start == "s":
    if num == 0:
        print("平手~")
    elif num == 1:
        print("你输了QQ")
    elif num == 2:
        print("恭喜你赢了！")
elif start == "r":
    if num == 1:
        print("平手~")
    elif num == 2:
        print("你输了QQ")
    elif num == 0:
        print("恭喜你赢了！")
elif start == "p":
    if num == 2:
        print("平手~")
    elif num == 0:
        print("你输了QQ")
    elif num == 1:
        print("恭喜你赢了！")


