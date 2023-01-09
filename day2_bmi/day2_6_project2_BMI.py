# BMI计算机

height = float(input("请输入您的身高（厘米）\n"))
weight = float(input("请输入您的体重（公斤）\n"))

bmi = weight / (height/100)**2
print(f"您的BMI是：{round(bmi,1)}")