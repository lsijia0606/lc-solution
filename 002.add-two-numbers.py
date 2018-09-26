
# coding: utf-8

# In[ ]:


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_over = 0
        dummy = end = ListNode(0)
        while l1 or l2 or carry_over:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry_over
            if val >= 10:
                carry_over = 1
                val = val - 10
            else:
                carry_over = 0
            end.next = ListNode(val)
            end = end.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


