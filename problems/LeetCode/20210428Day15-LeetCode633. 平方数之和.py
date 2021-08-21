# 第15天
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
import math

# 方法一，用b*b = c - a*a,判断b是否是平方数
# 数字的开方可以用1.pow(c,0.5);2.math.sqrt(c)
def judgeSquareSum(c: int) -> bool:
    if c == 0:
        return True
    for a in range(int(math.sqrt(c) + 1)):
        b = c - a * a
        if (int(math.sqrt(b)) ** 2) == b:
            return True
    return False

# 方法二，直接算，数字太大的话用时太多
def judgeSquareSum_2(c: int) -> bool:
    if c == 0:
        return True
    for a in range(int(math.sqrt(c) + 1)):
        for b in range(int(math.sqrt(c)) + 1):
            if (a*a + b*b) == c:
                return True
    return False


print(judgeSquareSum(5))
print(judgeSquareSum(2))
print(judgeSquareSum(999999999))