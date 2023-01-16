# 读取、写入档案

# 打开文件
# open("打开的文件", 打开的模式)
# 打开模式有r模式w模式a模式 read write add
# r读取
# w覆写
# a在原先的数据后再写东西

############################# 读取模式 #############################
file1 = open("123.txt","r")
print(file1.read())
file1.close()
  # 打开后一定要关闭这个档案
  # 不关闭的话会占用电脑资源  相当于今天玩了游戏snowrunner没有把它关掉又去玩了游戏stray

# 只读取文件的一行 file.readline() 只读取一行再回传回来
file1 = open("123.txt","r")
print(file1.readline())

# 想读取n行 readline n次执行
print(file1.readline())
print(file1.readline())
file1.close()

# 把文件里的数据一行一行读取出来 跑for循环
file1 = open("123.txt","r")
for line in file1:
    print(line)
file1.close()


############################# 覆写模式 #############################
file2 = open("456.txt", "w")
file2.write(f"123\n4325")       # .write()小括号里的就是覆写的内容 假设把档案覆写成123
file2.close()


############################# 增加模式 #############################
file3 = open("789.txt", "a")
file3.write("\nhello")
file3.write(" word")      # 同样用write函数
file3.write("\n小白")
file3.close()


# 若插入中文的时候出现乱码，可以encoding = "utf-8"
file3 = open("789.txt", "a", encoding="utf-8")
file3.close()


# 若觉得每次都要关闭很麻烦怕忘记 可有另一种写法
with open("789.txt", "a") as file3:
    file3.write("\n小白")
    # 冒号后面写要执行的操作 这样可以免去关闭的动作










