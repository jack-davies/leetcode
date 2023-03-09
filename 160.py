# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        lenA = 0
        while a is not None:
            a = a.next
            lenA += 1

        b = headB
        lenB = 0
        while b is not None:
            b = b.next
            lenB += 1

        diff = lenA - lenB
        a, b = headA, headB
        for i in range(diff):
            a = a.next
        for i in range(-diff):
            b = b.next

        i = 0
        while a is not None and b is not None:
            if a is b:
                return a
            a = a.next
            b = b.next
            i += 1

        return None
