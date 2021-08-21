# 第45天
#
# 给你两个单链表的头节点headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
# 图示两个链表在节点 c1 开始相交：
# 题目数据 保证 整个链式结构中不存在环。
# 注意，函数返回结果后，链表必须 保持其原始结构 。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = headA
        B = headB
        # A先遍历完链表headA,再开始遍历链表headB,到达相同节点node
        # B先遍历完链表headB,再开始遍历链表headA,到达相同节点node
        # 两者相等
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A