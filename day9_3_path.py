# 绝对路径 相对路径

# 绝对路径  ex: E:/Study\Python/1_fundamental1/day9_passwordmanager/123.txt
# 相对路径  根据目前程序的位置做延伸 ex: 123.txt

# 注意 Windows反斜线\要改成斜线/
# open后面绝对路径和相对路径都可以写

# 回到这个程序的上一个资料夹 ../../
with open("../day8_guessnumber/README.md") as md:
    print(md.read())



