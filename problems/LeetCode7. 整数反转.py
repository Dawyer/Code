#给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
class Solution:
    def reverse(self,x:int) -> int:
        if x < 0:
            y = 0 - int(str(x)[:0:-1])
        else:
            y = int(str(x)[::-1])

        if (y < -2 ** 31) or (y > 2 ** 31 - 1):
            return 0
        else:
            return y

a=Solution()
print(a.reverse(1534236469))