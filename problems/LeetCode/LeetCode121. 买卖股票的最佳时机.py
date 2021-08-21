# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

#暴力法
# def maxProfix(prices) -> int:
#     ans = 0
#     for i in range(len(prices)):
#         for j in range(i + 1, len(prices)):
#             ans = max(ans, prices[j] - prices[i])
#     return ans

def maxProfix(prices) -> int:
    inf = int(1e9)
    minprice = inf
    maxprofit = 0
    for price in prices:
        maxprofit=max(price - minprice,maxprofit)
        minprice=min(price,minprice)
    return maxprofit
print(maxProfix([7,1,5,3,6,4]))
print(maxProfix([6,5,4,3,2]))


