# 找出三个数字中最大的那个

def find_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        max = num1              # print(num1)也可
    elif num2 >= num1 and num2 >= num3:
        max = num2
    elif num3 >= num1 and num3 >= num2:
        max = num3
    print(max)

find_max(-80, 200, 20)
