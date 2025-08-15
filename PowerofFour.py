class Solution:
    def isPowerOfFour(self, n):
        return n > 0 and (n & n-1) == 0 and (n << 1).bit_length() % 2 == 0
