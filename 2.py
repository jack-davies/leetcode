# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 07:23:48 2018

@author: jckda
"""

class Solution:
    def getNumber(self, l):
        output = ""
        while l.next is not None:
            output += str(l.val)
            l = l.next
        return int(output + str(l.val))
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n = self.getNumber(l1) + self.getNumber(l2)
        print([int(x) for x in reversed(str(n))])