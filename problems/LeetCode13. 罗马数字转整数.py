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
    sum = 0
    luoma = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    teshu = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    for i in teshu.keys():
        if i in s:
            sum += teshu[i]
            s = s.replace(i,'')
    for j in luoma.keys():
        if j in s:
            sum += luoma[j] * s.count(j)
            s = s.replace(j, '')
    return sum

print(romanToInt('DXCIII'))