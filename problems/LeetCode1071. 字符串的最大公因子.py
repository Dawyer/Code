# 对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
#
# 返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
#
#  
#
# 示例 1：
#
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
# 示例 2：
#
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
# 示例 3：
#
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""
import math
#方法1
# def gcdOfString(str1:str,str2:str) -> str:
#     gcdString=''
#     for i in range(1,len(str1)+1):
#         str0=str1[0:i]
#         if str1 == str0 * (len(str1) // len(str0)) and str2 == str0 * (len(str2) // len(str0)):
#             if len(str0) > len(gcdString):
#                 gcdString=str0
#     return gcdString if gcdString != '' else ""

#方法1 提升，更快
# def gcdOfString(str1:str,str2:str) -> str:
#     for i in range(min(len(str1),len(str2)),0,-1):
#         if (len(str1) % i) == 0 and (len(str2) % i) == 0:
#             if str1[:i] * (len(str1) // i) == str1 and str1[:i] * (len(str2) // i) == str2:
#                 return str1[:i]
#     return ''

#方法2 求str1和str2的最大公约数
# def gcdOfString(str1:str,str2:str) -> str:
#     candidate_len=math.gcd(len(str1),len(str2))
#     candidate = str1[:candidate_len]
#     if candidate * (len(str1) // candidate_len) == str1 and candidate * (len(str2) // candidate_len) == str2:
#         return candidate
#     return ''

#方法3 str1和str2拼接后等于str2和str1的拼接
def gcdOfString(str1:str,str2:str) -> str:
    candidate_len=math.gcd(len(str1),len(str2))
    candidate=str1[:candidate_len]
    if str1 + str2 == str2 + str1:
        return candidate
    return ''
print(gcdOfString("ABCABC","ABC"))
print(gcdOfString("ABABAB","ABAB"))
print(gcdOfString("LEET","CODE"))
print(gcdOfString("AAAA","AAAAAAAA"))