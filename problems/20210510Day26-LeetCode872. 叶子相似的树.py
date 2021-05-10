# 第26天
#
# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
#    3
#   /  \
#   5   1
# /  \  / \
# 6  2  9  8
#   / \
#   7  4
# 举个例子，如上图所示，给定一棵叶值序列为(6, 7, 4, 9, 8)的树。
# 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是叶相似的。
# 如果给定的两个根结点分别为root1 和root2的树是叶相似的，则返回true；否则返回 false
# 示例 1：
# 输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# 输出：true
# 示例 2：
# 输入：root1 = [1], root2 = [1]
# 输出：true
# 示例 3：
# 输入：root1 = [1], root2 = [2]
# 输出：false
# 示例 4：
# 输入：root1 = [1,2], root2 = [2,2]
# 输出：true
# 示例 5：
# 输入：root1 = [1,2,3], root2 = [1,3,2]
# 输出：false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaf(res,root):
            if not root:return
            if not root.left and not root.right:
                res.append(root.val)
            leaf(res,root.left)
            leaf(res,root.right)

        res1 = []
        res2 = []
        leaf(res1,root1)
        leaf(res2,root2)
        return list(res1) == list(res2)