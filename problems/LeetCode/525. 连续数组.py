# 第44天
#
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
# 示例 1:
#
# 输入: nums = [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
# 示例 2:
# 输入: nums = [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # ans 结果, d 0与1个数的差值 下标, count [值,个数]
        ans, d, count = 0, {0: -1}, [0, 0]
        # i 下标, num 值
        for i, num in enumerate(nums):
            count[num] += 1
            # dict.setdefault(key, default=None)
            # key--查找的键值,default--键不存在时,设置的默认键值
            # setdefault(count[0] - count[1], i) 保存0与1个数差的最小下标
            # i - d.setdefault(count[0] - count[1], i) 长度
            ans = max(ans, i - d.setdefault(count[0] - count[1], i))
        return ans
