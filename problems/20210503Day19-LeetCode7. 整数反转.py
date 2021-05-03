# 第19天
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围[−231, 231− 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。

#
def reverse(x: int) -> int:
    a = 1
    if x < 0:
        a = 0
        y = str(x)[1:]
    else:
        y = str(x)
    y = int(y[::-1])
    if y > 2147483648:
        return 0
    if a == 0:
        y = 0 - y
    return y


print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(0))

