# for loop for循环
# for 变量名称 in 字串或列表


# 一一取出子串中的每一个字 用for和in之间的变量名称来代表它 再来执行
for variablename in "我是小白":
    print(variablename)
print("程式结束")
# 执行结果：
# 我
# 是
# 小
# 白
# 程式结束


# 取出列表里的每一个值
for name in ["小白", "小黑", "小绿"]:
    print(name)
    print(f"你好{name}")
# 执行结果
# 小白
# 你好小白
# 小黑
# 你好小黑
# 小绿
# 你好小绿


# 计算成绩总和
scores = [45, 67, 78, 90, 56, 24, 65, 100, 56, 89]
sum = 0
for score in scores:
    sum += score
print(f"学生成绩总和为{sum}分")


# 通常会把in前的名称取为in后复数名称的单数形式
