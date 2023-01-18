# json 模块
# json是一个数据格式 json模块可以帮助我们再读档和写档的时候更加方便
# dumps indent load

# 现有一个字典
# password = {
#     "account": "123",
#     "password": "456"
# }


# 把它写进passward.txt
'''
with open("password.txt", "a") as file:
    file.write(password)
这样做会出错 因为写入文件的只能是字符串
转成字符串是可以的 也可以通过read取得这个字典
    file.write(str(password))
但现在取得的字典仍然是一个字串 所以还是没办法对它取值的 比如
    x = file.read()
    print(x["account"])
会报错 因为字串不是字典 没办法取值
是否能转换成字典呢
    x = dict(file.read())
    print(x["account"])
仍然是错误 因为没办法把哪个字串转换成字典
'''



# 这时json模块就能派上用场了
'''
json是内建模块 可直接引入
json模块有提供函数 可以把数据转换成json格式的字串去做储存
也有提供函数可以帮我们把读取出来的字串再转换回Python的格式
'''

# dumps用法
# json.dumps(xxxx)  把xxxx的数据转换成json格式的字串
# json.dumps(xxxx, indent=n)  想要让文件中的也做缩进 n是缩进的空格数

import json
password = {
    "account": "123",
    "password": "456"
}

with open("password.json", "w") as f:
    f.write(json.dumps(password, indent=4))

# json.loads()可以把json格式的字串转换回Python格式的数据
# 此处password.txt中的字串在python格式中是字典 所以转换回python格式后就是字典
with open("password.txt", "r") as f:
    x = json.loads(f.read())
    print(x)
    print(x["account"])
    print(x["password"])

with open("password.txt", "a") as p:
    list = [1, 2, 3, 4, 5]
    p.write(json.dumps(list))


# 若文件写入的是json格式的数据 后缀改成.json会比较清楚
# 若现在写入的档案是一个原本没有的档案的话 便会创建一个档案出来



