class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        point = len(matrix)//2
        p1 = 0
        p2 = len(matrix[0])-1

        for _ in range(point):
            if matrix[point][-1] > target and matrix[point][0] > target:
                if point == 0:
                    return False
                point -= 1
            elif matrix[point][-1] < target and matrix[point][0] < target:
                if point == len(matrix)-1:
                    return False
                point += 1

        while p1 <= p2:
            p = ((p2-p1)//2)+p1

            if matrix[point][p] == target:
                    return True
            elif matrix[point][p] > target:
                    p2 = p-1
            elif matrix[point][p] < target:
                    p1 = p+1
            
        return False
