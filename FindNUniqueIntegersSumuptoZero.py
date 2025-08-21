class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = [0]*n
        p1 = 0 
        p2 = n-1
        m = 1
        if n % 2 != 0: 
            l[p1] = 0
            p1 += 1
        while p1 < p2:
                l[p1] = m
                l[p2] = -m
                m += 1
                p2 -= 1
                p1 += 1
        return l
