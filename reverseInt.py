class Solution(object):
    def reverse(self, x):
        result = 0
        negativo = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x // 10

            if result > (2**31 - 1) // 10:
                return 0

            result = result * 10 + digit

        return -result if negativo else result
        
        