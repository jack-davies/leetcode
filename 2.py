# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getNumber(self, l):
        output = ""
        while l.next is not None:
            output += str(l.val)
            l = l.next
        output += str(l.val)
        output = int(output[::-1])
        return output

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = self.getNumber(l1) + self.getNumber(l2)
        return [int(x) for x in str(n)[::-1]]
