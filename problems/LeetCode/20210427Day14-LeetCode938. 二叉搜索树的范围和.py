# 第14天
#
# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
#

# 中序遍历得到递增列表，再求left和right之间值的和


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.res = []
        self.InOrder(root)
        self.sum = 0
        for i in self.res:
            if i >= low and i <= high:
                self.sum += i
        return self.sum

    def InOrder(self,root):
        if not root:
            return
        self.InOrder(root.left)
        self.res.append(root.val)
        self.InOrder(root.right)