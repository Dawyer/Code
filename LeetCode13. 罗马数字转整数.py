# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

def romanToInt(s:str) -> int:
    sum=0
    