# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]


def spiralOrder(matrix):
    spiral = []
    while matrix:
        for i in (matrix.pop(0)):
            spiral.append(i)
        matrix = list(zip(*matrix))[::-1]
    return spiral


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix1),spiralOrder(matrix2))