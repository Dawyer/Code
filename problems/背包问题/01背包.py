"""
第49天

有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。
输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。
"""
from typing import List
class solution:
    def max_value(self, N: int, V: int, v: List[int], w: List[int]):
        # dp = [[0 for j in range(V + 1)] for i in range(N + 1)]
        dp = [[0] * (V+1) for i in range(N+1)]
        for i in range(1, N+1):  # i取1到N
            for j in range(1, V+1):  # j取1到V
                dp[i][j] = dp[i - 1][j]  # 不选第i个
                if j >= v[i-1]:  # 选第i个
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i-1]] + w[i-1])
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    s = solution()
    print(s.max_value(4, 5, [1, 2, 3, 4], [2, 4, 4, 5]))
