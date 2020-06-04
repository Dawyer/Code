# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6

# 方法一 暴力
# def trap(height) -> int:
#     ans = 0
#     for i in range(len(height)):
#         max_left, max_right = 0, 0
#         for j in range(0, i):
#             max_left = max(max_left, height[j])
#         for j in range(i, len(height)):
#             max_right = max(max_right, height[j])
#         if min(max_left, max_right) > height[i]:
#             ans += min(max_left, max_right) - height[i]
#     return ans


# 方法二 动态规划
# def trap(height) -> int:
#     # 边界条件
#     if not height:
#         return 0
#     n = len(height)
#     maxleft = [0] * n
#     maxright = [0] * n
#     ans = 0
#     # 初始化
#     maxleft[0] = height[0]
#     maxright[n-1] = height[n-1]
#     # 设置备忘录，分别储存左边和右边最高的柱子的高度
#     for i in range(1, n):
#         maxleft[i] = max(height[i], maxleft[i-1])
#     for j in range(n-2, -1, -1):
#         maxright[j] = max(height[j], maxright[j+1])
#     # 一趟遍历，比较每个位置可以存储多少水
#     for i in range(n):
#         if min(maxleft[i], maxright[i]) > height[i]:
#             ans += min(maxleft[i], maxright[i]) - height[i]
#     return ans

# 方法三 双指针法
def trap(height) -> int:
    if not height:
        return 0
    n = len(height)
    left, right = 0, n-1
    maxleft, maxright = height[0], height[n-1]
    ans = 0
    while left <= right:
        maxleft = max(height[left], maxleft)
        maxright = max(height[right], maxright)
        if maxleft < maxright:
            ans += maxleft - height[left]
            left += 1
        else:
            ans += maxright - height[right]
            right -= 1
    return ans

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))