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

def longestCommonPrefix(strs):
    longestCommon = ''
    for i in range(len(strs[0])):
        comm = strs[0][0:i+1]
        print('comm:{}'.format(comm))
        for j in strs[1:]:
            count = 1
            print('j:{}'.format(j))
            if comm in j:
                print('ok')
                count += 1
                if count < len(strs)-1:
                    continue
                else:
                    longestCommon = comm
    return longestCommon

print(longestCommonPrefix(["flower","flow","flight"]))