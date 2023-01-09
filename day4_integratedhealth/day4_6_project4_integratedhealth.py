# 综合健康计算机（BMI BMR TDEE）


def get_bmi():
    height = float(input("请输入您的身高(公分)"))
    weight = float(input("请输入您的体重(公斤)"))
    bmi = round(weight / (height / 100) ** 2, 1)
    return f"您的BMI：{bmi}"

def get_bmr():
    sex = input("请输入您的性别(男or女)")
    height = float(input("请输入您的身高(公分)"))
    weight = float(input("请输入您的体重(公斤)"))
    age = float(input("请输入您的年龄"))
    if sex == "男":
        bmr = round(66 + 13.7 * weight + 5 * height - 6.8* age, 2)
    else:
        bmr = round(655 + 9.6 * weight + 1.8 * height - 4.7 * age, 2)
    return f"您的基础代谢率(BMR)：{bmr}"

def get_tdee():
    sex = input("请输入您的性别(男or女)")
    height = float(input("请输入您的身高(公分)"))
    weight = float(input("请输入您的体重(公斤)"))
    age = float(input("请输入您的年龄"))
    if sex == "男":
        bmr = round(66 + 13.7 * weight + 5 * height - 6.8 * age, 2)
    else:
        bmr = round(655 + 9.6 * weight + 1.8 * height - 4.7 * age, 2)
    print("(1)久坐、几乎没运动")
    print("(2)每周低强度运动1~3天")
    print("(3)每周中强度运动3~5天")
    print("(4)每周高强度运动6~7天")
    print("(5)劳力密集工作或是每天高强度训练")
    choice = input("请选择您的运动量 (输入1~5)")
    if choice == "1":
        tdee = bmr * 1.2
    elif choice == "2":
        tdee = bmr * 1.375
    elif choice == "2":
        tdee = bmr * 1.55
    elif choice == "2":
        tdee = bmr * 1.725
    else:
        tdee = bmr * 1.9
    tdee = round(tdee, 2)
    return f"您的总热量消耗(TDEE)：{tdee}"

print("欢迎使用综合健康计算机~")
print("(1)计算bmi")
print("(2)计算基础代谢率(bmr)")
print("(3)计算总热量消耗(tdee)")
pro_cho = input("请选择要计算的项目 (输入：1 or 2 or 3)")

if pro_cho == "1":
    result = get_bmi()
elif pro_cho == "2":
    result = get_bmr()
else:
    result = get_tdee()
print(result)
