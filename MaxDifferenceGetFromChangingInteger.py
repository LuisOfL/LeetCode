class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        n1 = next((x for x in s if x != '9'),s[0])
        maxN = int(s.replace(n1,'9'))

        if s[0] != '1':
            minN = int(s.replace(s[0],'1'))
        else:
            for ch in s[1:]:
                if ch != '0' and ch != '1':
                    minN = int(s.replace(ch, '0'))
                    break
            else:
                minN = int(s)

        return maxN - minN
