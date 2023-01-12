# 测验2
# 做一个程序 从下面三位学生里面随机挑选一位并印出这个人的资料

students = {
    "小白": {
        "age": 23,
        "height": 170.5,
        "weight": 60
    },
    "小黄": {
        "age": 30,
        "height": 160.55,
        "weight": 38
    },
    "小绿": {
        "age": 15,
        "height": 160.5,
        "weight": 38
    },
}

def lottery():
    print(f"抽到的是：{list(students)[n]}")
    print(f"年纪：{list(list(students.values())[n].values())[0]}")
    print(f"身高：{list(list(students.values())[n].values())[1]}")
    print(f"体重：{list(list(students.values())[n].values())[2]}")

import random

n = random.randint(0, 2)
lottery()















