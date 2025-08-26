class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        max_d = 0
        max_a = 0 
        for a,b in dimensions:
            n = (a**2+b**2)**0.5
            area = a*b
            if n > max_d:
                max_d = n
                max_a = area
            elif n == max_d:
                if area > max_a:
                    max_a = area
        return max_a
