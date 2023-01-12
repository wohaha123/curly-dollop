# 把名字抽出来放到一个变量里 再用这个名字去取值

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

import random
stu_name = list(students)
random_name = stu_name[random.randint(0,2)]
print(f"抽到的是：{random_name}")
print(f'年纪：{students[random_name]["age"]}')
print(f'身高：{students[random_name]["height"]}')
print(f'体重：{students[random_name]["weight"]}')

