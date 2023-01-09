# 改良BMI计算机 day2_6_project2_BMI.py
# 除了计算出bmi还要判断这个人的体重状况

height = float(input("请输入您的身高（厘米）\n"))
weight = float(input("请输入您的体重（公斤）\n"))

bmi = weight / (height/100)**2
print(f"您的BMI是：{round(bmi,1)}")

if bmi < 18.5:
    print("体重过轻！")
elif bmi < 24:
    print("正常体重！")
elif bmi < 27:
    print("体重过重！")
elif bmi < 30:
    print("轻度肥胖！")
elif bmi < 35:
    print("中度肥胖！")
else:
    print("重度肥胖!")


# 不用写elif bmi >= 18.5 and bmi < 24:因为条件语句是从上往下一个一个依次判断