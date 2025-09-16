class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = [[1]]
        if numRows == 1:
            return l
        for i in range(1,numRows):
            temp = []
            for p1 in range(i+1):
                if p1 == i or p1 == 0:
                    temp.append(1)
                    continue
                temp.append(l[i-1][p1]+l[i-1][p1-1])
            l.append(temp)
        return l
