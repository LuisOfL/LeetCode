class Solution(object):
    def zeroFilledSubarray(self, nums):
        total = 0
        count = 0
        for i in nums:
            if i == 0:
                count = count + 1
                total = total + count
            else:
                count = 0
        return total
