class Solution(object):
    def myPow(self, x, n):
        
        tot = 1
        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = -n

        while n > 0:
            if n % 2 == 1:
                tot *= x
            x *= x
            n //= 2

        return tot
        
