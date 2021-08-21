# 第41天
#
# 两个整数的汉明距离 指的是这两个数字的二进制数对应位不同的数量。
# 计算一个数组中，任意两个数之间汉明距离的总和。
# 示例:
# 输入: 4, 14, 2
# 输出: 6
# 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.


# 若长度为 nn 的数组 \textit{nums}nums 的所有元素二进制的第 ii 位共有 cc 个 11，
# n-cn−c 个 00，则些元素在二进制的第 ii 位上的汉明距离之和为
#
# c⋅(n−c)

from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                res += bin(nums[i] ^ nums[j]).count("1")
        return res