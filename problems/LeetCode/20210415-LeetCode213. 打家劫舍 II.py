# 刷题第3天，(o-ωｑ)).oO 困
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
# 示例 1：
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 示例 2：
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 3：
# 输入：nums = [0]
# 输出：0
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

# 好难 😂
# 参考的官方答案
#
# 用动态规划，能想出状态转移方程 dp[i]=max(dp[i−2]+nums[i],dp[i−1])
# 还有边界条件 dp[start]=nums[start]                         只有一间房屋，则偷窃该房屋
#            dp[start+1]=max(nums[start],nums[start+1])    只有两间房屋，偷窃其中金额较高的房屋
#  还有首尾相连，所有取(start,end)=(0,n−2) 和 (start,end)=(1,n−1)进行计算，取最大值
#
#
#
#

def rob(nums):
    def robRange(start,end):
        first = nums[start]
        second = max(nums[start], nums[start+1])
        for i in range(start+2,end+1):
            first, second = second, max(first+nums[i], second)
        return second

    length = len(nums)
    if length == 1:
        return nums[0]
    elif length == 2:
        return max(nums[0], nums[1])
    else:
        return max(robRange(0, length-2),robRange(1,length-1))


num1 = [2,3,2]
num2 = [1,2,3,1]
print(rob(num1))
print(rob(num2))