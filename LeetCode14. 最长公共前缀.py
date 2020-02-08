# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
# 所有输入只包含小写字母 a-z 。

#Solution 1
# def longestCommonPrefix(strs):
#     if not strs:return ""  #strs为空返回空
#     s1 = min(strs)  #s1赋值为最小的字符串
#     s2 = max(strs)  #s2赋值为最大的字符串
#     for i,x in enumerate(s1):
#         if x != s2[i]:
#             return s2[:i]
#     return s1

#Solution 2
def longestCommonPrefix(strs):
    if not strs:return ""
    ss = list(map(set,zip(*strs)))  #zip(*strs)与zip(strs)相反，逆解压
    res = ""
    for i,x in enumerate(ss):
        x = list(x)
        if len(x) > 1:
            break
        res = res + x[0]
    return res

print(longestCommonPrefix(["flower","flow","flight"]))