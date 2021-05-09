# 给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组[4,-1,2,1] 的和最大，为6 。
# 示例 2：
# 输入：nums = [1]
# 输出：1
# 示例 3：
# 输入：nums = [0]
# 输出：0
# 示例 4：
# 输入：nums = [-1]
# 输出：-1
# 示例 5：
# 输入：nums = [-100000]
# 输出：-100000
from typing import List
# def maxSubArray(nums: List[int]) -> int:
#     for i in range(1,len(nums)):
#         print(i,nums[i-1])
#         nums[i] = nums[i] + max(nums[i-1],0)
#     return nums


def maxSubArray(nums: List[int]) -> int:
    pre = 0
    max_ans = nums[0]
    for i in range(0, len(nums)):
        pre = max(pre+nums[i], nums[i])
        max_ans = max(pre, max_ans)
    return max_ans
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([5,4,-1,7,8]))