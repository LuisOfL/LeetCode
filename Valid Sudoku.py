class Solution(object):
    def isValidSudoku(self, board):
       row = []
       colum = []
       dic = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
       for x in range(9):
        row = []
        colum = []
        for y in range(9):
            if board[x][y].isdigit():
                row.append(board[x][y])
                if x < 3 and y < 3:
                    dic[1].append(board[x][y])
                if x < 3 and y < 6 and y >= 3:
                    dic[2].append(board[x][y])
                if x < 3 and y < 9 and y >= 6:
                    dic[3].append(board[x][y])
                if x < 6 and y < 3 and x >= 3:
                    dic[4].append(board[x][y])
                if x < 6 and y < 6 and x >= 3 and y >= 3:
                    dic[5].append(board[x][y])
                if x < 6 and y < 9 and x >= 3 and y >= 6:
                    dic[6].append(board[x][y])
                if x < 9 and y < 3 and x >= 6:
                    dic[7].append(board[x][y])
                if x < 9 and y < 6 and x >= 6 and y >= 3:
                    dic[8].append(board[x][y])
                if x < 9 and y < 9 and x >= 6 and y >= 6:
                    dic[9].append(board[x][y])

            if board[y][x].isdigit():
                colum.append(board[y][x])
        temp = set(row)
        temp1 = set(colum)
        if len(row) != len(temp):
            return False
        if len(colum) != len(temp1):
            return False
        
        for x in dic.values():
            temp = set(x)
            if len(x) != len(temp):
                return False

       return True
