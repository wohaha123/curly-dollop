# 测验3 1-100所有偶数总和

sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)

sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)


