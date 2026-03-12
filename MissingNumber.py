class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in range(max(nums)):
            if x not in nums:
                return x
        return max(nums)+1
