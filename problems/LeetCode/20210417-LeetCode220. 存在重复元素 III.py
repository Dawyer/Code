# Day5,周末加油

# 给你一个整数数组 nums 和两个整数 k 和 t 。
# 请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，
# 同时又满足 abs(i - j) <= k 。
# 如果存在则返回 true，不存在返回 false。
# 示例 1：
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
# 示例 2：
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
# 示例 3：
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false

# 自己写的代码超时了，菜鸡就是这样
# 用滑动窗口解决问题，学到了

def containsNearbyAlmostDuplicate(nums, k, t):
    for i in range(len(nums)):
        for j in range(i + 1, min(i + k + 1, len(nums))):
            if abs(nums[i] - nums[j]) <= t:
                return True
    return False


print(containsNearbyAlmostDuplicate([1,2,3,1],3,0))
print(containsNearbyAlmostDuplicate([1,0,1,1],1,2))
print(containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))