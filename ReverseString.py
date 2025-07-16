class Solution(object):
    def reverseString(self, s):
        start = 0
        fin = len(s)-1
        while start < fin:
            temp = s[start]
            s[start] = s[fin]
            s[fin] = temp
            start += 1
            fin -= 1
        return s
