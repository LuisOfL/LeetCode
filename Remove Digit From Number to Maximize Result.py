class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        l = []
        for x in range(len(number)):
            if number[x] == digit:
                temp = number[:x] + number[x+1:]
                l.append(temp)
        return max(l)
