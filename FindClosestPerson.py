class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        n1 = abs(z-x)
        n2 = abs(z-y)
        if n1 > n2:
            return 2
        elif n1 < n2:
            return 1
        elif n1 == n2:
            return 0
