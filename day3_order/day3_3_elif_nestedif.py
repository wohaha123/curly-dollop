# elif（否则如果）、nested if(嵌套 if)

# 如果 你的分数>90：
#     我就给你100元
# 否则如果 你的分数>80：
#     我就给你50元
# 否则如果 你的分数>70：
#     我就给你30元
# 否则：
#     你给我100元

score = float(input("请输入您的考试分数：\n"))
cheat = input("请输入该人是否作弊：(T or F)\n")
if cheat == "T":
    cheat = True
elif cheat == "F":
    cheat = False
else:
    print("输入错误，请重新输入！")
    quit()
if score > 90:
    if cheat:
        print("作弊不给钱")
    else:
        print("我就给你100元")
elif score > 80:
    if cheat:
        print("作弊不给钱")
    else:
        print("我就给你50元")
elif score > 70:
    if cheat:
        print("作弊不给钱")
    else:
        print("我就给你30元")
else:
    print("你给我100元")