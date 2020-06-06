# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#  
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
#
# 限制：
#
# 0 <= matrix.length <= 100
# 0 <= matrix[i].length <= 100


class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return matrix

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        #visited=[[False, False, False], [False, False, False], [False, False, False]]
        total = rows * columns
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0

        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution_1 = Solution()
print(solution_1.spiralOrder(matrix))