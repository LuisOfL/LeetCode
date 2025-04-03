class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return True
            else:
                dic[num] = i
        return False