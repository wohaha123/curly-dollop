# 测验一

# 假设是商店老板，字典存的是客户和他们的消费总金额
# 用for循环去跑过字典里的每一个值
# 只要客户的消费总金额>=10000，将对应的值改成VIP
# 反之 将对应值改成一般客户

customer_spending = {
    "小白": 2000,
    "小黑": 3000,
    "小黄": 12000,
    "小绿": 15000,
    "小灰": 8000
}

for customer in customer_spending:
    if customer_spending[customer] >= 10000:
        customer_spending[customer] = "VIP"
    else:
        customer_spending[customer] = "一般客户"

print(customer_spending)


