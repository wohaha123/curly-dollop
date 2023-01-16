# 测验1
# 做一个程序 可以读取档案里的所有数字 把他们做相加 最后再印出来


with open("test1.txt", "r") as txt:
    sum = 0
    for num in txt:
        print(num)
        sum += int(num)
print(sum)








