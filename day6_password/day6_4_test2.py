# 测验2 找出最高分


# 方法一（自己想的）
# max(list) 返回列表元素中的最大值
# 字符转数字，见stringTOnumber.py
scores_str = input("请输入学生成绩(中间用,隔开)\n")
scores = scores_str.split(",")

scores_list = []
for score in scores:
    scores_list.append(int(score))

print(f"最高分是：{max(scores_list)}")


# 方法二（小白）
# 新建一个变量赋值为0，代替
scores_str = input("请输入学生成绩(中间用,隔开)\n")
scores = scores_str.split(",")

highest_score = 0
for score in scores:
    if int(score) >= highest_score:
        highest_score = int(score)

print(f"最高分是：{highest_score}")


