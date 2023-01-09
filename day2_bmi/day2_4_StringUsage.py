# 一些字串用法

'''
字串里面要用双引号
解决办法：
1.把外面的双引号变成单引号
2.在里面的双引号左边加上反斜线  \"
'''

print('他今年“25"岁')
print("他今年\"25\"岁")


'''
字串里面要做换行
解决办法：
\n
'''

input("请输入您的名字\n")


'''
想在字串里面使用其他的数据类型
解决办法：
f-string
'''

age = 25
height = 170.5
is_male = True
print("小白今年" + str(age) + "岁，身高" + str(height) + "，是否为男性" + str(is_male))
print(f"小白今年{age}岁，身高{height}，是否为男性{is_male}")