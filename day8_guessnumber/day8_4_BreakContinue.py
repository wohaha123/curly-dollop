# 循环用法 break continue
# 在循环中写 break 可直接跳出循环
# 在循环里写 continue 可直接进入下一次循环


# =========================break=========================

# 想在i = 3时直接跳出循环
for i in range(1, 6):
    print(i)
    if i == 3:
        break
print("跳出循环")

# break也可以用在while循环
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
print("跳出循环")

# break有什么用呢？
# 类似于这种情况 如果有人考满分 就停下来了 在数据量很大的时候可以加快速度
highest = 0
for score in [20, 30, 40, 50, 100, 45, 100, 40]:
    if score == 100:
        highest = 100
        break
    if score > highest:
        highest = score
print(highest)



# =========================continue=========================

highest = 0
for score in [20, 30, 40, 50, 100, 45, 100, 40]:
    if score == 30:
        continue
    print(score)
#  continue直接跳到下一个循环可理解为跳过该次循环不执行


# while循环也可
i = 1
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
print("跳出循环")


