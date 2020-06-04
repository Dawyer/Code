# 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
#
# 如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
#
# 你允许：
#
# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空
# 示例 1: (From the famous "Die Hard" example)
#
# 输入: x = 3, y = 5, z = 4
# 输出: True
# 示例 2:
#
# 输入: x = 2, y = 6, z = 5
# 输出: False
import math
#深度优先搜索
# def canMeasureWater(x:int,y:int,z:int) -> bool:
#     stack=[(0,0)]
#     seen=set()
#     while stack:
#         remain_x,remain_y = stack.pop()
#         if remain_x == z or remain_y == z or remain_x+remain_y == z:
#             return True
#         if(remain_x,remain_y) in seen:
#             continue
#         seen.add((remain_x,remain_y))
#         stack.append((x,remain_y))
#         stack.append((remain_x,y))
#         stack.append((0,remain_y))
#         stack.append((remain_x,0))
#
#         stack.append((remain_x - min(remain_x,y-remain_y),remain_y + min(remain_x,y - remain_y)))
#         stack.append((remain_x + min(remain_y,x-remain_x),remain_y - min(remain_y,x - remain_x)))
#     return False

#最大公约数
def canMeasureWater(x,y,z) -> bool:
    if x+y <z:
        return False
    if x == 0 or y == 0:
        return z == 0 or x + y == z
    return z % math.gcd(x,y) == 0

print(canMeasureWater(3,5,4))
print(canMeasureWater(2,6,5))