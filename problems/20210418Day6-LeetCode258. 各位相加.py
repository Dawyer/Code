# Day6 第3题

# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
# 示例:
# 输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
# 进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗


# 一开始想到用递归，将每次数的各位相加知道小于10
# 进阶方法说不能使用循环或者递归，看了网友的评论，可以找到其中的规律
# s1 = 100*a+10*b+c,s2=a+b+c
# s1-s2 = 99a+9b 发现是9的倍数
def addDigits(num):
    if num < 10:
        return num
    sum = 0
    for i in str(num):
        sum += int(i)
    return addDigits(sum)


def advance_addDigits(num):
    if num > 9:
        num = num % 9
        if num == 0:
            return 9
    return num


print(addDigits(38))
print(addDigits(38))