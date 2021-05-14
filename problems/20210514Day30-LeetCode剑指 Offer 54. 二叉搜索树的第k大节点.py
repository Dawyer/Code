# 给定一棵二叉搜索树，请找出其中第k大的节点。
# 示例 1:
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#   2
# 输出: 4
# 示例 2:
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.arr = []
        self.middle(root)
        n = len(self.arr)
        return self.arr[n - k]

    def middle(self,root):
        if not root:
            return
        self.middle(root.left)
        self.arr.append(root.val)
        self.middle(root.right)