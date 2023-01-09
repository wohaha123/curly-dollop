# 综合健康计算机（BMI BMR TDEE）
# 教学答案 更简单
# 先分别定义三个函数 再分别弄他们的


def get_bmi(height, weight):
    height /= 100
    bmi = weight / height ** 2
    bmi = round(bmi, 1)
    return bmi

def get_bmr(sex, height, weight, age):
    if sex == "男":
        bmr = 66 + 13.7 * weight + 5 * height - 6.8 * age
    else:
        bmr = 655 + 9.6 * weight + 1.8 * height - 4.7 * age
    bmr = round(bmr, 2)
    return bmr

def get_tdee(sex, height, weight, age, times):
    bmr = get_bmr(sex, height, weight, age)
    tdee = bmr * times
    tdee = round(tdee, 2)
    return tdee



print("欢迎使用综合健康计算机~")
print("(1)计算bmi")
print("(2)计算基础代谢率(bmr)")
print("(3)计算总热量消耗(tdee)")
number = input("请选择要计算的项目 (输入：1 or 2 or 3)")

if number == "1":
    height = float(input("请输入您的身高(公分)"))
    weight = float(input("请输入您的体重(公斤)"))
    bmi = get_bmi(height, weight)
    print(f"您的BMI：{bmi}")
elif number == "2":
    sex = input("请输入您的性别(男or女)")
    height = float(input("请输入您的身高(公分)"))
    weight = float(input("请输入您的体重(公斤)"))
    age = int(input("请输入您的年龄"))
    bmr = get_bmr(sex, height, weight, age)
    print(f"您的基础代谢率(BMR)：{bmr}")
elif number == "3":
    sex = input("请输入您的性别(男or女)")
    height = float(input("请输入您的身高(公分)"))
    weight = float(input("请输入您的体重(公斤)"))
    age = float(input("请输入您的年龄"))
    print("(1)久坐、几乎没运动")
    print("(2)每周低强度运动1~3天")
    print("(3)每周中强度运动3~5天")
    print("(4)每周高强度运动6~7天")
    print("(5)劳力密集工作或是每天高强度训练")
    exer = input("请选择您的运动量 (输入1~5)")
    times = 0
    if exer == "1":
        times = 1.2
    elif exer == "2":
        times = 1.375
    elif exer == "3":
        times = 1.55
    elif exer == "4":
        times = 1.725
    else:
        times = 1.9

    tdee = get_tdee(sex, height, weight, age, times)
    print(f"您的总热量消耗(TDEE)：{tdee}")