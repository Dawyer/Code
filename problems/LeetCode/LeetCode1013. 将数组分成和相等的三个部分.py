# 给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
#
# 形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
#
# 示例 1：
#
# 输出：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 示例 2：
#
# 输入：[0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
# 示例 3：
#
# 输入：[3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

#方法一:时间超时
# def canThreePartsEqualSum(A) -> bool:
#     result = 0
#     for x in range(1,len(A)):
#         for y in range(x+1,len(A)):
#             print("x={},y={}" .format(x,y))
#             print("sum(A[0:x]={},sum(A[x:y])={},sum(A[y:-1])={}" .format(sum(A[0:x]),sum(A[x:y]),sum(A[y:])))
#             if (sum(A[0:x]) == sum(A[x:y])) & (sum(A[0:x]) == sum(A[y:])) :
#                 result = 1
#                 break
#     return True if result == 1 else False

#方法二
def canThreePartsEqualSum(A) -> bool:
    s=sum(A)
    if s%3 != 0:return False
    target=s//3
    n,i,cur=len(A),0,0
    while i < n:
        cur += A[i]
        if cur == target:break
        i += 1
    if cur != target:return False
    j = i+1
    while j+1 < n:
        cur += A[j]
        if cur == target * 2:return True
        j += 1
    return False

print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
print(canThreePartsEqualSum([1,-1,1,-1]))
