# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        current = head
        while current is not None:
            current = current.next
            length += 1

        neg1 = ListNode(None, head)
        left = neg1
        right = head.next

        for _ in range(length-n):
            left = left.next
            right = right.next

        left.next = right

        return neg1.next
