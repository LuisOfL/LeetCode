class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = ''
        k = 1
        for x in str(num):
            if k and x == '6':
                ans += '9'
                k -= 1
            else:
                ans += x
        return int(ans)
