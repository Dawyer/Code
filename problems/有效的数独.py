# 请你判断一个9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
# 数字1-9在每一行只能出现一次。
# 数字1-9在每一列只能出现一次。
# 数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用'.'表示。
from typing import List
class Solution:
    def isValidSudoku(self, board: List[int]) -> bool:
        row = [[] * 9 for _ in range(9)]
        col = [[] * 9 for _ in range(9)]
        nine = [[] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                tmp = board[i][j]
                if not tmp.isdigit():
                    continue
                if tmp in row[i]:
                    return False
                if tmp in col[j]:
                    return False
                if tmp in nine[(j // 3) * 3 + (i // 3)]:
                    return False
                row[i].append(tmp)
                col[j].append(tmp)
                nine[(j // 3) * 3 + (i // 3)].append(tmp)
        return True

s = Solution()
board = [[".","8","7","6","5","4","3","2","1"]
    ,["2",".",".",".",".",".",".",".","."]
    ,["3",".",".",".",".",".",".",".","."]
    ,["4",".",".",".",".",".",".",".","."]
    ,["5",".",".",".",".",".",".",".","."]
    ,["6",".",".",".",".",".",".",".","."]
    ,["7",".",".",".",".",".",".",".","."]
    ,["8",".",".",".",".",".",".",".","."]
    ,["9",".",".",".",".",".",".",".","."]]
print(s.isValidSudoku(board))