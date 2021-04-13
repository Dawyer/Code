# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 示例 1：
#        4
#   	/ \
#      2   6
#     / \
#    1   3
# 输入：root = [4,2,6,1,3]
# 输出：1
# 示例 2：
#        1
#   	/ \
#      0   48
#          / \
#        12   49
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
# 提示：
# 树中节点数目在范围 [2, 100] 内
# 0 <= Node.val <= 105

# 以后每天刷题，冲！！！
# 注意这是BST，中序遍历的话是有序的
# 先中序遍历再进行比较
# 二叉树的题还是不会做，要学会二叉树的遍历，遍历后将二叉树转换成列表
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.vals = []
        self.order(root)
        n = len(self.vals)
        # 由于vals是有序的，对相邻的2个值求差，取最小
        return min([self.vals[i + 1] - self.vals[i] for i in range(n - 1)])

# 中序遍历
    def order(self, root):
        if root == None:
            return
        self.order(root.left)
        self.vals.append(root.val)
        self.order(root.right)



