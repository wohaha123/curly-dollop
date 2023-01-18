# 密码管理器

# 做了几个函数
# 判断值是否存在于列表中：if name in ["123", "456", "798"]  如果有存在则会回传True给我们
# 将json档案清空后会出现解析错误 原因是json是空的再用loads做解析的话会发生错误
# 所以将json做解析之前应该先判断档案是不是一个空字串

import json
def get_password_dic():             # 读取已经存在的passxxx.json中的数据
    with open("passxxxxProject.json", "r") as f:
        password_str = f.read()
        if password_str == "":
            return{}
        else:
            return json.loads(password_str)     # 回传读取出来的东西哦 之后用函数可以直接取值

def check_name(name):               # 检查name是否已经存在于子哦点的函数
    password_dic = get_password_dic()              # 先去取得文件中的字典
    if name in password_dic.keys():                  # 使用.keys来取得数据中的所有keys 会回传给我们一个列表类似于["google", "fb", "netflix"]
        return False        # 没有使用过
    else:
        return True         #有使用过

def add_password(name, account, password):          # 添加一组账号密码的函数
    if check_name(name):
        password_dic = get_password_dic()           # 使用读取json函数防止之后写入的数据会覆盖 且使字典等于读取出来的字典
        password_dic[name] = {
                    "account": account,
                    "password": password
                }                                   # 写入字典
        with open("passxxxxProject.json", "w") as f:
            f.write(json.dumps(password_dic))           # 写入json
        return True         # 表示新增成功
    else:
        return False        # 表示已经使用过了

print("欢迎使用密码管理器~")

while True:         # 做一个循环可重复请问要使用什么功能呢？（r查询 a新增 q离开）
    mode = input("请问要使用什么功能呢？（r查询 a新增 q离开）")
    if mode == "q":
        break
    elif mode == "a":
        name = input("请输入账号名称：")
        account = input("请输入账号：")
        password = input("请输入密码：")
        if add_password(name, account, password):
            print("新增成功~")
        else:
            print("已有此账号名称")
    elif mode == "r":
        name = input("请输入账号名称：")
        if check_name(name):
            print("无此账号名称")
        else:
            password_dic = get_password_dic()
            account = password_dic[name]["account"]
            password = password_dic[name]["password"]
            print(f"账号：{account}，密码：{password}")



