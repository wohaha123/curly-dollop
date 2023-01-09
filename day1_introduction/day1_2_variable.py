# 变量 variable

'''
变量的命名规则
1.只能是字母数字下划线的组合  （字母不仅限于英文字母，中日韩文等都可以）
2.开头不能是数字
3.不能是关键字
'''



name = "小绿"

print(name + "今年68岁")
print("早上起床" + name + "吃了汉堡")
print(name + "说汉堡好吃")
print("刚刚" + name + "去上厕所")

# 印出两行使用者的年龄
age = input("请输入您的年龄：")
print(age)
print(age)

# 变量的值也可以随时随地做改变
score = "50"
print(score)
score = "80"
print(score)




# test 2   交换 number1 和 number2

number1 = input("请输入第一个数字：")
number2 = input("请输入第二个数字：")

temper = number1
number1 = number2
number2 = temper

print("number1 = " + number1)
print("number2 = " + number2)