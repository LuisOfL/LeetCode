class Solution(object):
    def subsets(self, nums):
        subsets = []
        n = len(nums)
        for i in range(2**n):
            temp = []
            for j in range(n):
                if (i >> j) & 1:  
                    temp.append(nums[j])
            subsets.append(temp)
        return subsets
