# 第12天
#
# 给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，
# 使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
# 示例1：
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
# 实例2：
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.tree = []
        self.InorderTraversal(root)
        if not self.tree:
            return
        dummy = TreeNode(-1)
        cur = dummy
        for node in self.tree:
            node.left = node.right = None
            cur.right = node
            cur = cur.right
        return dummy.right

    def InorderTraversal(self,root):
        if not root:
            return
        self.InorderTraversal(root.left)
        self.tree.append(root)
        self.InorderTraversal(root.right)
