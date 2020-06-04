# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
#
# 不占用额外内存空间能否做到？
#
#  
#
# 示例 1:
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:
#
# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]


#方法一，数组
# def rotate(matrix) -> None:
#     n = len(matrix)
#     matrix_new = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             matrix_new[j][n-i-1] = matrix[i][j]
#     matrix[:] = matrix_new

#方法二，用翻转代替旋转
def rotate(matrix) -> None:
    n = len(matrix)
    #水平翻转
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
    #主对角线翻转
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]