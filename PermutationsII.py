class Solution(object):
    def permuteUnique(self, nums):
        used = set()
        if len(nums) == 1:
            return [nums[:]]
        
        res = []
        for i in range(len(nums)):
            if not nums[i] in used:
                used.add(nums[i])
                n = nums.pop(i)
                perms = self.permuteUnique(nums)
                for perm in perms:
                    perm.append(n)
                res.extend(perms)
                nums.insert(i, n)
        return res
