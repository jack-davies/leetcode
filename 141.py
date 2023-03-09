# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            # 0, 1 case
            return False

        pulse1, pulse2 = head, head
        i = 1
        while True:
            # Advance two pulses, one at half speed
            pulse1 = pulse1.next
            if i % 2 == 0:
                pulse2 = pulse2.next

            if pulse1.next is None:
                return False

            if pulse1 is pulse2:
                return True

            i += 1
