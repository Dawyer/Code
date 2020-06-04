# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2

import collections
#方法一，用set()减少重复的元素，再比较数量
# def majorityElement(nums) -> int:
#     elements=[]
#     for i in set(nums):elements.append(i)
#     for element in elements:
#         if nums.count(element) > (len(nums) // 2):
#             return element

#方法二 用哈希映射存储每个元素以及出现的次数
# def majorityElement(nums):
#     counts = collections.Counter(nums)
#     return max(counts.keys(),key=counts.get)


#方法三 排序法
def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]


print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))