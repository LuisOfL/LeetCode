# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        def lenght(lis):
            p = 0
            current = lis
            while current:
                p += 1
                current = current.next
            return p

        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        n1 = lenght(head)

        for _ in range(n1-n):
            current = current.next

        current.next = current.next.next
        return dummy.next
