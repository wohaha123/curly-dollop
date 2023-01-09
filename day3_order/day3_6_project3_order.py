# 拉面点餐系统
# 全部变大写  .upper()
# 全部变小写  .lower()
# print("AbCd".upper())

print("欢迎使用拉面点餐机~")
print("(1)盐味拉面 $220")
print("(2)酱油拉面 $240")
print("(3)豚骨拉面 $280")
taste = input("请选择拉面口味 (输入：1 or 2 or 3)")

big = input("是否加大，豚骨口味+$50，其他口味+$30 (输入：Y or N)").upper()
egg = input("是否加糖心蛋+$30 (输入：Y or N)").upper()
char = input("是否加叉烧+$60 (输入：Y or N)").upper()

price = 0

if taste == "1":
    price += 220
elif taste == "2":
    price += 240
else:
    price += 280

if big == "Y" and taste == "3":
    price += 50
else:
    price += 30

if egg == "Y":
    price += 30

if char == "Y":
    price += 60

if big == "Y" and egg == "Y" and char == "Y":
    price -= 20
    print(f"\n加好加满折扣$20，总金额${price}，感谢您的光临！")
else:
    print(f"\n总金额${price}，感谢您的光临！")