class Solution(object):
    def minMaxDifference(self, num):
        s = str(num)
        n1 = next((c for c in s if c != '9'), s[0])
        maxN = int(s.replace(n1,'9'))
        minN = int(s.replace(s[0], '0'))
        return maxN - minN
