class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        mat = []
        for x in range(n):
            temp = []
            for y in range(n):
                temp.append(matrix[y][x])
            mat.append(temp)
        
        for x in range(n):
            for y in range(n):
                matrix[x][y] = mat[x][(n-1)-y]
        return matrix
