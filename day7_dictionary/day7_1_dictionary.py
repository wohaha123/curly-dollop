# 字典 dictionary   可储存很多键跟值的配对
# 数据类型：dictionary dict

#   键      值
#  key    value
# "苹果"  "apple"

# 格式：dataname = {key1: value1, key2: value2, ....}
# 说明：key value什么类型都可


# 做字典
eng_dic = {
    "苹果": "apple",
    "香蕉": "banana",
    "猫": "cat",
    "age": 23,
    "score": 98,
    "is_male": True,
    0: "你好",
    2.34: "哈哈"
}
print(type(eng_dic))
print(eng_dic)


# 查字典
# 取出值value
print(eng_dic["苹果"])
print(eng_dic["age"])
print(eng_dic["score"])
print(eng_dic["is_male"])
print(eng_dic[0])
print(eng_dic[2.34])


# 改掉键对应的值
eng_dic[0] = "哈哈哈"
print(eng_dic[0])


# 增加键对应的值
eng_dic[1] = "哈哈哈哈"
print(eng_dic[1])
print(eng_dic)


# 字典也像列表一样可以搭配for循环使用
for item in eng_dic:
    print(item)
# 运行结果：会印出字典里的所有键


# 想印出字典里的所有值
for item in eng_dic:
    print(eng_dic[item])





