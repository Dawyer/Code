"""
有 N种物品和一个容量是 V 的背包，每种物品都有无限件可用。
第 i 种物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值
"""
from typing import List
def max_value(N: int, V: int, v: List[int], w: List[int]):
    dp = [0 for i in range(V+1)]
    for i in range(N):
        for j in range(v[i],V+1):
            dp[j] = max(dp[j],dp[j-v[i]] + w[i])
    return dp[-1]
print(max_value(4, 5, [1, 2, 3, 4], [2, 4, 4, 5]))