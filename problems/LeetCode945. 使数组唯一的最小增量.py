# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
#
# 返回使 A 中的每个值都是唯一的最少操作次数。
#
# 示例 1:
#
# 输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
# 示例 2:
#
# 输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
# 提示：
#
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000

class Solution:
    def __init__(self):
        pass
    def minIncrementForUnique_1(self,A) -> int:
        A.sort()
        count = 0
        for i in range(1,len(A)):
            if A[i] <= A[i-1]:
                count += A[i-1] - A[i] + 1
                A[i] = A[i-1] + 1
        return count

    def minIncrementForUnique_2(self,A):
        A.sort()
        A.append(100000)
        ans = taken = 0
        for i in range(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += give * (give+1) // 2 + give * A[i-1]
                taken -= give
        return ans

list_1=[1,2,2]
list_2=[3,2,1,2,1,7]
Solution_1=Solution()
Solution_2=Solution()
print(Solution_1.minIncrementForUnique_2(list_1))
print(Solution_2.minIncrementForUnique_2(list_2))
