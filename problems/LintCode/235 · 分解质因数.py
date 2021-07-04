"""
第59天
描述
将一个整数分解为若干质因数之乘积。
"""
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # 因数最大值为num的开方
        up = int(num ** 0.5 + 1)
        res = []
        # 遍历从2到up,num能整除的话增加到列表中
        # 循环除以i直到不能被整除
        # 因为是从小到大遍历，必定只有质数能被取为因数
        for i in range(2, up):
            while num % i == 0:
                res += [i]
                num //= i
        if num > 1:
            res.append(num)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.primeFactorization(1008918916563456))