# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            proposed = current.next
            while proposed and current.val == proposed.val:
                proposed = proposed.next
            current.next = proposed
            current = current.next

        return head
