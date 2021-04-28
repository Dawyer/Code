#
# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。
# 例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
# 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
from typing import List


def addToArrayForm(num: List[int], k: int) -> List[int]:
    sum_num = 0
    res = []
    if k == 0:
        return num
    for i in num:
        sum_num *= 10
        sum_num += i
    sum_num += k
    while sum_num:
        res.append(sum_num % 10)
        sum_num //= 10
    return res[::-1]

# 第二种方法
# 将list A中的元素换成字符，合并后更改为int类型，与K相加后，变字符型,int,最后为list
# 学到用map更改类型
def addToArrayForm_2(A, K):
    return list(map(int, str(int(''.join(map(str, A))) + K)))


print(addToArrayForm([0], 0))
print(addToArrayForm([1,2,0,0], 34))
print(addToArrayForm([2,7,4], 181))
print(addToArrayForm([2,1,5], 806))
print(addToArrayForm([9,9,9,9,9,9,9,9,9,9], 1))