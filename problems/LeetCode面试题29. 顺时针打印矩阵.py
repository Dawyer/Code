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


class Solution1:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return matrix
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row = 0
        column = 0
        directionIndex = 0

        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            row_next = row + direction[directionIndex][0]
            column_next = column + direction[directionIndex][1]

            if not (0 <= row_next < rows and 0 <= column_next < columns and not visited[row_next][column_next]):
                directionIndex = (directionIndex+1) % 4

            row = row + direction[directionIndex][0]
            column = column + direction[directionIndex][1]

        return order


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
solution_1 = Solution1()
solution_2 = Solution1()
print(solution_1.spiralOrder(matrix),solution_2.spiralOrder(matrix2))