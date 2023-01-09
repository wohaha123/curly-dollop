# 函数回传 return
# 回传的值会覆盖掉原来的呼叫
# 函数遇到return会直接回传 不会继续下面的的代码

def find_max(num1, num2, num3):
    if type(num1) != int or type(num2) != int or type(num3) != int:
        return "请输入整数！"
    if num1 >= num2 and num1 >= num3:
        return num1              # print(num1)也可
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num3 >= num1 and num3 >= num2:
        return num3
    print(max)
    return 45645


max1 = find_max(-80, 200, 20)
print(max1)     # 是否要return会影响该值