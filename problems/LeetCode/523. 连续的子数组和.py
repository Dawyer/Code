# 第43天
#
# 给你一个整数数组 nums 和一个整数k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
# 子数组大小 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 如果存在，返回 true ；否则，返回 false 。
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。
#
# 示例 1：
# 输入：nums = [23,2,4,6,7], k = 6
# 输出：true
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
# 示例 2：
# 输入：nums = [23,2,6,4,7], k = 6
# 输出：true
# 解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
# 42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
# 示例 3：
# 输入：nums = [23,2,6,4,7], k = 13
# 输出：false

'''
        在每个索引位置i, 计算当前和对k的mod值, 假设在索引x处, sum[0~x] = m*k + mod_x;
        在索引y处, sum[0~y] = n*k + mod_y; 如果mod_x == mod_y且y-x > 1说明sum[x~y]
        即为一个符合要求的连续子数组, 用map来保存每个mod值对应的索引, 一旦出现新的mod值出现
        在map中, 判断索引差是否大于1.
        注意特殊情况:
        1) 当nums中有连续0, 无论k为何值都是正确的;
        2) 除情况1之外出现k为0都是错误的;
        3) k为负数也是可能的, 但是要将其变为对应正数来求mod.
        此外需要在map中初始化<0,-1>, 其原因在于解决到达某个i时sum恰好可以整除k的情况, 选择-1
        的原因是要求连续子数组长度大于等于2, 这样可以避免第一个数字为0的情况
'''
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modeset = set()
        presum = 0
        for num in nums:
            presum += num
            if (presum % k) in modeset:
                return True
            modeset.add((presum - num) % k)
        return False