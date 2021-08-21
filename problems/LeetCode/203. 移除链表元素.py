# 第46天
#
# 给你一个链表的头节点 head 和一个整数 val ，
# 请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 递归
class Solution1:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # head为空，返回head
        if head is None:
            return head
        # removeElements返回下一个Node节点
        head.next = self.removeElements(head.next, val)
        # head 的值与val相等，head指向head.next
        if head.val == val:
            head = head.next
        else:
            head = head
        return head

# 迭代
class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p is not None:
            if p.next and p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next

