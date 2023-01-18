# 密码管理器
# 没写出来的地方有: 无此账号、账号已存在的地方
# 判断key是否存在于字典中：http://c.biancheng.net/view/2212.html

import json
pw_data = {}

print("欢迎使用密码管理器~")

i = 1
while i == 1:
    func = input("请问要使用什么功能呢？（r查询 a新增 q离开）")
    if func == "a":
        name = input("请输入账号名称：")
        account = input("请输入账号：")
        passward = input("请输入密码：")
        pw_data[name] = {"account": account, "password": passward}
        with open("passxxxxProject.json", "a") as passxxxx:
            passxxxx.write(json.dumps(pw_data, indent=4))
            print("新增成功~")
    elif func == "r":
        name = input("请输入账号名称：")
        with open("passxxxxProject.json", "r") as passxxxx:
            x = json.loads(passxxxx.read())
            print(f"账号：{x[name]['account']}, 密码：{x[name]['password']}")
    elif func == "q":
        i = 0




