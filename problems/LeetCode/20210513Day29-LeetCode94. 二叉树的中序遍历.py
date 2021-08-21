# 第29天
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.arr = []
        self.middle(root)
        return self.arr

    def middle(self,root):
        if not root:
            return
        self.middle(root.left)
        self.arr.append(root.val)
        self.middle(root.right)