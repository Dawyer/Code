# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  
#
# 示例：
#
# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]

def generateParenthesis(n:int):
    if n == 0:
        return ['']
    ans = []
    for c in range(n):
        for left in generateParenthesis(c):
            for right in generateParenthesis(n-1-c):
                ans.append('({}){}'.format(left, right))
    return ans


