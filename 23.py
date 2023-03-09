# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2(l1: ListNode, l2: ListNode) -> ListNode:
            start = ListNode(None, None)
            current = start
            while True:
                if l2 is None:
                    current.next = l1
                    return start.next
                elif l1 is None:
                    current.next = l2
                    return start.next
                elif l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

        def combine(l: List[ListNode]) -> List[ListNode]:
            if len(l) == 0:
                return [None]
            elif len(l) == 1:
                return l
            elif len(l) == 2:
                return [merge2(l[0], l[1])]
            else:
                return combine(combine(l[:len(l)//2]) + combine(l[len(l)//2:]))

        return combine(lists)[0]
