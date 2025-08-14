class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        p1, p2 = 0, 2
        max_n = ""  

        while p2 < len(num):
            if num[p1] == num[p1+1] == num[p2]:
                max_t = num[p1]  
                if max_t > max_n:
                    max_n = max_t
            p1 += 1
            p2 += 1

        return max_n * 3 if max_n else ""
