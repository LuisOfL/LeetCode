class Solution(object):
    def moveZeroes(self, nums):
       pos = 0
       for x in range(len(nums)):
            if nums[x] != 0:
                nums[pos] = nums[x]
                pos += 1

       while pos < len(nums):
            nums[pos] = 0
            pos += 1
