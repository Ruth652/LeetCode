class Solution(object):
    def isToeplitzMatrix(self, matrix):
        if len(matrix) == 1:
            return True
        
        col = len(matrix[0])
        
        for i in range(len(matrix) - 1):
            for j in range(col - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        
        return True
