# 英文单词练习机

# random.sample 多用于截取列表的指定长度的随机数，但是不会改变列表本身的排序
# random.sample(list, n) 在list里面抽取n个值出来 返回抽取出的值组成的列表

eng_dic = {
    "蘋果": "apple",
    "香蕉": "banana",
    "貓": "cat",
    "狗": "dog",
    "蛋": "egg",
    "食物": "food",
    "遊戲": "game",
    "手": "hand",
    "冰": "ice",
    "果醬": "jam",
    "國王": "king",
    "標籤": "label",
    "郵件": "mail",
    "脖子": "neck",
    "油": "oil",
    "豬": "pig",
    "皇后": "queen"
}

import random

# 共17题

# 把题抽出来
# lot_nums_list: 抽取出nums道题 随机排列 的 keys 列表
nums = int(input("请问要练习几题？"))
lot_nums_list = random.sample(list(eng_dic), nums)
random.shuffle(lot_nums_list)

n = 0       # 保存的答对了n题的数据
for i in range(0, nums):
    print(f"第{i+1}题")
    guess = input(f"请问'{lot_nums_list[i]}'的英文是：")
    if guess == f"{eng_dic[f'{lot_nums_list[i]}']}":
        print("恭喜答对")
        n += 1
    else:
        print(f"答错了~ 答案为：{eng_dic[f'{lot_nums_list[i]}']}")

print(f"总共{nums}题 答对了{n}题")









