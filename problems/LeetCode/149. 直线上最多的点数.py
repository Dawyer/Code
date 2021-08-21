"""
第56天
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
"""
from collections import Counter
from math import inf
from typing import List
class Solution:
    def maxPoint(self, points:List[List[int]]) -> int:
        # 求出每2点的斜率，统计相同斜率的数量
        ans = 1
        for i in range(len(points) - 1):
            # 用Counter()方法统计各个斜率的数量
            curr = Counter()
            for j in range(i+1, len(points)):
                # 计算两点间x,y的差
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                # 计算斜率时要考虑x坐标相同的情况，此时斜率为无穷大
                curr[dy / dx if dx else -1] += 1
            # 只有一个点，len(points)=1时，ans=1
            ans = max(ans, max(curr.values()) + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxPoint([[1,1],]))
    print(s.maxPoint([[1,1],[2,2],[3,2],[4,3]]))
    print(s.maxPoint([[1,1],[2,2],[3,3]]))
    print(s.maxPoint([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))