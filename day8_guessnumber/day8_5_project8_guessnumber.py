# 猜数字游戏
# str.isdigit() 如果 string 中只包含数字字符，则返回 True，否则返回 False
# 浮点数判断的异常处理

import random


print("欢迎来到猜数字游戏")
print("谜底为1~100随机的一个整数（最多5次猜测机会）")

# 在1-100里抽出一个整数answer作为猜测的答案
answer = random.randint(1, 100)
i = 0
for n in range(1, 7):
    i += 1
    if i == 6:
        print(f"你输了~ 超出猜测次数\n谜底为{answer}")
        break
    print(f"第{n}次猜测")
    guess = input("请输入猜测的数字：")
    if not str.isdigit(guess):                # str.isdigit()
        print("只能输入整数")
        continue
    else:
        guess = int(guess)
    if guess > answer:
        print("再小一点")
    elif guess < answer:
        print("再大一点")
    else:
        print("恭喜答对")
        break




