class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        p1 = 0
        max_tot = 0
        max_temp = 0
        for p2,c in enumerate(s):
            while len(s[p1:p2+1]) != len(set(s[p1:p2+1])):
                p1 += 1
            max_temp = len(s[p1:p2+1])
            if max_temp > max_tot:
                max_tot = max_temp
        return max_tot
