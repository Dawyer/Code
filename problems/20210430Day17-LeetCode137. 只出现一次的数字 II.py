# 第17天 4月的最后一天
#
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，
# 其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
from typing import List
import collections
nums_1 = [2, 2, 3, 2]
nums_2 = [0, 1, 0, 1, 0, 1, 99]


def singleNumber(nums: List[int]) -> int:
    freq = collections.Counter(nums)
    print(freq.items())
    # ans = [num for num, occ in freq.items() if occ == 1][0]
    for num, occ in freq.items():
        if occ == 1:
            ans = num
    return ans



print(singleNumber(nums_1))
# print(singleNumber(nums_2))