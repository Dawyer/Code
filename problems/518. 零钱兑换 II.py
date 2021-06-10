"""
第50天
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

示例 1:
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:
输入: amount = 10, coins = [10] 
输出: 1
"""
from typing import List
class Solution:
    def change_1(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for i in range(amount + 1)] for j in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(amount + 1):
                dp[i][j] = dp[i-1][j]
                k = 1
                while k * coins[i-1] <= j:
                    dp[i][j] += dp[i - 1][j - k * coins[i - 1]]
                    k += 1
        return dp

    def change_2(self, amount: int, coins: List[int]) -> int:
        # dp[i] 表示金额之和等于i的金币组合数
        dp = [0 for i in range(amount + 1)]
        # 金额为0时的组合数为1，0个金币时金额为0
        dp[0] = 1
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] += dp[j - i]
        return dp

if __name__ == '__main__':
    s = Solution()
    print(s.change_2(5, [1,2,5]))
    print(s.change_1(5, [1,2,5]))
    print(s.change_2(3, [2]))