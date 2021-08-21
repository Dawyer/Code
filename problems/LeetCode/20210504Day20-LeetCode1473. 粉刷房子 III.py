# 第20天
#
# 在一个小城市里，有m个房子排成一排，你需要给每个房子涂上 n种颜色之一（颜色编号为 1 到 n）。
# 有的房子去年夏天已经涂过颜色了，所以这些房子不需要被重新涂色。
# 我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 houses = [1,2,2,3,3,2,1,1] ，
# 它包含 5 个街区 [{1}, {2,2}, {3,3}, {2}, {1,1}] 。）
# 给你一个数组houses，一个m * n的矩阵cost和一个整数target，其中：
# houses[i]：是第i个房子的颜色，0表示这个房子还没有被涂色。
# cost[i][j]：是将第i个房子涂成颜色j+1的花费。
# 请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成target个街区。如果没有可用的涂色方案，请返回-1。
# 示例 1：
# 输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# 输出：9
# 解释：房子涂色方案为 [1,2,2,1,1]
# 此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
# 涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
# 示例 2：
# 输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# 输出：11
# 解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
# 此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
# 给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
# 示例 3：
# 输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
# 输出：5
# 示例 4：
# 输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
# 输出：-1
# 解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。
from typing import List

class Solution:
    def minCost(self, houses: List[int], cost: List[int], m: int, n: int, target: int) -> int:
        houses = [c - 1 for c in houses]
        dp = [[[float("inf")] * target for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue
                for k in range(target):
                    for j0 in range(n):
                        if j == j0:
                            if i == 0:
                                if k == 0:
                                    dp[i][j][k] = 0
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
                        elif i > 0 and k > 0:
                            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j0][k-1])
                    if dp[i][j][k] != float("inf") and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]
        ans = min(dp[m-1][j][target-1] for j in range(n))
        return -1 if ans == float("inf") else ans