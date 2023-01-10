# random 模块
# 模组（模块） module

import module_health           #引入模块

bmr = module_health.get_bmr("男", 170.5, 62, 40)
print(bmr)

print(module_health.a)
print(module_health.b)

import random

num = 7 * random.random()
print(num)