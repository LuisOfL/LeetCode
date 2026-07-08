class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(numbers)):
            com = target - numbers[i]
            if com in dic:
                return [dic[com]+1,i+1]
            else:
                dic[numbers[i]] = i
        return False
