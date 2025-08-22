class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p1 = 0
        p2 = len(nums)-1
        while p1 <= p2:
            m = (p1 + p2)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                p1 = m+1
            else:
                p2 = m-1
        return -1
