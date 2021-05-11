# 第27题
#
# 给你一个整数数组perm，它是前n个正整数的排列，且n是个 奇数。
# 它被加密成另一个长度为 n - 1的整数数组encoded，满足encoded[i] = perm[i] XOR perm[i + 1]。
# 比方说，如果perm = [1,3,2]，那么encoded = [2,1]。
# 给你encoded数组，请你返回原始数组perm。题目保证答案存在且唯一。
# 示例 1：
# 输入：encoded = [3,1]
# 输出：[1,2,3]
# 解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
# 示例 2：
# 输入：encoded = [6,5,4,6]
# 输出：[2,4,1,5,3]
from functools import reduce
from operator import xor
from typing import List
def decode(encoded: List[int]) -> List[int]:
    n = len(encoded) + 1
    total = reduce(xor, range(1, n+1))
    odd = 0
    for i in range(1, n-1, 2):
        odd ^= encoded[i]
    perm = [total ^ odd]
    for i in range(n-1):
        perm.append(perm[-1] ^ encoded[i])
    return perm

print(decode([6,5,4,6]))