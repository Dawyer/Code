# 第11天
#
# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
# 题目数据保证答案符合 32 位整数范围。
# 示例 1：
# 输入：nums = [1,2,3], target = 4
# 输出：7
# 解释：
# 所有可能的组合为：
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 请注意，顺序不同的序列被视作不同的组合。
# 示例 2：
# 输入：nums = [9], target = 3
# 输出：0
# 提示：
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# nums 中的所有元素 互不相同
# 1 <= target <= 1000

def combinationSum4(nums, target):
    dp = [0] * (target + 1)  # 长度为target+1的数组
    dp[0] = 1  # target=0时为1
    for i in range(target+1):  # 要算i值就要算出i前面元素的值
        for num in nums:  # 每次都要遍历一次nums的值
            if i >= num:  # 当i大于num中的元素时，就能拆分i
                dp[i] += dp[i-num]  # 将拆分后的i的值相加，得到的值存入dp数组
    return dp[target]  # 返回target值
print(combinationSum4([1,2,3],4))

# 本题是数组的元素和与目标值相等，首先想到的是递归，递归所用时间长，然后想到动态规划
# 此题是可以重复使用数组元素，如果不能重复使用怎么办？--可以将num排序，从小到大赋值

