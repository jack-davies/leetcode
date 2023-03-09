# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l2 is None:
            return l1
        elif l1 is None:
            return l2

        if l2.val < l1.val:
            current = l2
            l2 = l2.next
        else:
            current = l1
            l1 = l1.next
        start = current

        while True:
            if l1 is None:
                current.next = l2
                break
            elif l2 is None:
                current.next = l1
                break
            elif l2.val < l1.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next

        return start
