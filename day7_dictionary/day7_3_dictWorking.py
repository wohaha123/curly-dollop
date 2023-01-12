# 字典用法

#   键      值
#  key    value


# value可以是列表
# value可以是字典

student = {
    "name": ["小白", "小黑", "小绿"],
    "age": {
        "小白": 23,
        "小黑": 30,
        "小绿": 28
    }
}
print(student["name"][1])   # 取出"小黑"
print(student["age"]["小黑"])    # 取出小黑的年龄


# 可以在列表里面写字典
studens_list = [
    {
        "name": "小白",
        "age": 23
    },
    {
        "name": "小黑",
        "age": 30
    },
    {
        "name": "小绿",
        "age": 28
    }
]
print(studens_list[0]["name"])    # 取得name对应的小白
print(studens_list[0]["age"])




# =========================== 列表常搭配的函数 ====================================================================

# keys
# dictname.keys()
# 可取得字典里的所有key
print(student.keys())
print(student.values())
# print(student.keys()[0])  该函数不能取值  TypeError: 'dict_keys' object is not subscriptable
# 若想取值 可转换成列表
print(list(student.keys()))     # 转列表
print(list(student.keys())[0])  # 取值

# 转换成列表也会取出字典里的所有key
print(list(student))





