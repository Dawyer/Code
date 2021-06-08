"""
第48天

有一堆石头，用整数数组stones 表示。其中stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为x 和y，且x <= y。那么粉碎的可能结果如下：

如果x == y，那么两块石头都会被完全粉碎；
如果x != y，那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。
"""
from functools import lru_cache
from math import inf
from typing import List
class Solution:
    def lastStoneWeight(self, stones:List[int]) -> int:
        '''
        1.dfs深度优先算法：Depth First Search
        2.@functools.lru_cache(maxsize=None,typed=False)
        maxsize为最多缓存的次数，如果为None则无限制;如果typed=True则不同类型的参数调用将分别缓存
        '''
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == len(stones):
                return curr if curr >=0 else inf
            return min(dfs(idx+1, curr+stones[idx]), dfs(idx+1, curr-stones[idx]))
        return dfs(0,0)

if __name__ == '__main__':
    s = Solution()
    print(s.lastStoneWeight([2,7,4,1,8,1]))
    print(s.lastStoneWeight([1,1,4,2,2]))
