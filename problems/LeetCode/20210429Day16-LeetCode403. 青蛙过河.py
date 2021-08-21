# 第16天
#
# 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。
# 青蛙可以跳上石子，但是不可以跳入水中。
# 给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。
# 开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。
# 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。
#  另请注意，青蛙只能向前方（终点的方向）跳跃。
import functools
from typing import List

stones_1 = [0, 1, 3, 5, 6, 8, 12, 17]
stones_2 = [0, 1, 2, 3, 4, 8, 9, 11]


def canCross(stones: List[int]) -> bool:
    if stones[1] - stones[0] > 1: return False
    stonesSet = set(stones)  # 变成Set， 加速检索

    @functools.lru_cache(None)  # 加上备忘录，去掉重复计算
    def helper(i, step):
        # 状态，表示当前是第几块石头，是走几步走过来的。
        if i == stones[-1]:
            return True
        # 选择， 走 step + 1 步， 走 step 步，还是走step - 1 步？，
        # 只要往前走的步数有石头（在数组内），就试着可以往前走
        if i + step + 1 in stonesSet:
            if helper(i + step + 1, step + 1):
                return True
        if i + step in stonesSet:
            if helper(i + step, step):
                return True
        if step - 1 > 0 and i + step - 1 in stonesSet:
            # 这边要检查一下，step -1 要大于0 才走
            if helper(i + step - 1, step - 1):
                return True
        return False
    return helper(stones[1], stones[1] - stones[0])


print(canCross(stones_1))
print(canCross(stones_2))
