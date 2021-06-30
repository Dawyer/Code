"""
第57天

输入一个正整数N， 你需要按样例的方式返回一个字符串列表。
"""

def printX(n):
    A = []
    for i in range(n):
        lin_n = ""
        for j in range(n):
            if j == i or j == n-1-i:
                lin_n = lin_n + "X"
            else:
                lin_n = lin_n + " "
        print(lin_n)
        A.append(lin_n)
    return A

print(printX(10))