# 判断输入的一个整数是奇数还是偶数

num = int(input("请输入一个整数：\n"))
temp = num % 2
if temp == 0:
    print("您输入的数为偶数")
else:
    print("您输入的数为奇数")