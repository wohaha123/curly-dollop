# 嵌套列表 nested list

nums = [1, 2, 3, [1, 2, 3, [1, 2, 3]]]

print(nums[3][3][1])        # 取得嵌套list里的值（该表为三维列表）


# n*n的二维列表
list2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(list2d[1][2])