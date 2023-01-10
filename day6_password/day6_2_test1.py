# 测验1 改良day2的project:bmi计算机
# 使之计算无数多次直到使用者输入n为止

def bmi():
    height = float(input("请输入您的身高（厘米）\n"))
    weight = float(input("请输入您的体重（公斤）\n"))
    bmi = weight / (height/100)**2
    print(f"您的BMI是：{round(bmi,1)}")

bmi()

go = input("请问还要再计算吗：(请输入 y or n)").lower()
while go == "y":
    bmi()
    go = input("请问还要再计算吗：(请输入 y or n)")


