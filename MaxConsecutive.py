class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0
        temp = 0
        for x in nums:
            if x == 1:
                temp += 1
            else:
                if temp > maxi:
                    maxi = temp
                temp = 0
        if temp > maxi:
                    maxi = temp
        return maxi
