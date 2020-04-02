# 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
#
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
#
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
#
#  
#
# 示例：
#
# 输入：
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# 输出：
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

def gameOfLife(board) -> None:
    neighors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
    rows = len(board)
    cols = len(board[0])

    copy_borad = [[board[row][col] for col in range(cols)] for row in range(rows)]
    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0
            for neighor in neighors:
                r = (row + neighor[0])
                c = (col + neighor[1])
                if (r < rows and r>= 0) and (c < cols and c >= 0) and (copy_borad[r][c] == 1):
                    live_neighbors += 1
            if copy_borad[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[row][col] = 0
            if copy_borad[row][col] == 0 and live_neighbors == 3:
                board[row][col] = 1