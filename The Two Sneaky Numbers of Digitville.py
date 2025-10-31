class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen  = set()
        res = []
        for x in nums:
            if x in seen:
                res.append(x)
            else:
                seen.add(x)
        return res
