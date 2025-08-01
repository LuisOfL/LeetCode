class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c = 0
        maX = 0
        l = []
        for x in range(len(nums1)):
            c = 0
            for y in range(len(nums2)):
                if nums2[y] == nums1[x]: 
                    maX = nums2[y]
                    c = 1
                if nums2[y] > maX and c == 1:
                    l.append(nums2[y])
                    break
                if y == len(nums2)-1:
                    l.append(-1)
        return l
