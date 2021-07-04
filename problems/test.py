import functools
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        res = []
        if isA(num):
            return [num]
        else:
            while num != 1:
                for i in range(2, num+1):
                    if isA(i) and num % i == 0:
                        res.append(i)
                        num = num // i
                        break
        return res

@functools.lru_cache
def isA(num):
    if num == 2:
        return True
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.primeFactorization(100891891))
