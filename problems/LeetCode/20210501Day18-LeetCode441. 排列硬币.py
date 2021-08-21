# 你总共有n枚硬币，你需要将它们摆成一个阶梯形状，第k行就必须正好有k枚硬币。
#
# 给定一个数字n，找出可形成完整阶梯行的总行数。
#
# n是一个非负整数，并且在32位有符号整型的范围内。

class Solution():
    def arrangeCoins(self, n: int) -> int:
        self.res = 1
        self.df(n)
        return self.res

    def df(self, n):
        if n < self.res:
            self.res -= 1
            return
        else:
            n = n - self.res
            self.res += 1
            self.df(n)


n = Solution()
print(n.arrangeCoins(5))
print(n.arrangeCoins(8))
