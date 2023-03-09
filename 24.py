# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        start = head.next

        while True:
            try:
                first = head
                second = head.next
                third = second.next
                fourth = third.next
                fifth = fourth.next  # ensures fourth is not None

                second.next = first
                first.next = fourth

                head = third

            except AttributeError:
                # no pointers changed in try block
                if first is None:
                    pass
                elif second is None:
                    pass
                elif third is None:
                    second.next = first
                    first.next = None
                elif fourth is None:
                    second.next = first
                    first.next = third

                return start
