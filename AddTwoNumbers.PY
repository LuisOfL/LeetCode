# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p = 1
        tot_1,tot_2 = 0,0
        n1,n2 =0,0
        while l1:
            n1 = l1.val
            tot_1 = tot_1 + n1*p
            p *= 10
            l1 = l1.next
            if l1 is None:
                break
        p = 1
        while l2:
            n2 = l2.val
            tot_2 = tot_2 + n2*p
            p *= 10
            l2 = l2.next
            if l2 is None:
                break
        total = tot_1+tot_2
        dummy = ListNode(0)
        current = dummy
        if total == 0:
            return ListNode(0)

        while total > 0:
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            total //= 10
        return dummy.next
