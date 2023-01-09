# 逻辑运算(and, or, not)

# 如果 分数1考100分 且 分数2也考100分：
#     我给你100元
#     我带你出去玩

'''
score1 = float(input("请输入科目1的分数"))
score2 = float(input("请输入科目2的分数"))
if score1 == 100 and score2 == 100:
    print("我给你100元")
    print("我带你出去玩")
'''


# 如果 分数1考100分 或 分数2考100分
#     我给你100元
#     我带你出去玩

'''
if score1 == 100 or score2 == 100:
    print("我给你100元")
    print("我带你出去玩")
else:
    print("都没考100分")
'''


# 如果 分数1没有考100分：
#     你给我100元

score1 = float(input("请输入科目1的分数：\n"))
if not score1 == 100:
    print("你给我100元")

# 可以写!=100  或  if not score1 == 100: