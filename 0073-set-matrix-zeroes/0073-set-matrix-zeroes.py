class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero, first_col_zero = False, False
        
        # if the first row or first column need to be zeroed
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
                
        for j in range(cols): 
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Use first row and column to mark zero rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Zero out marked rows and columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out the first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
        # Zero out the first row if needed
        if first_row_zero:73
            for j in range(cols):
                matrix[0][j] = 0
                
                
#Question: https://leetcode.com/problems/set-matrix-zeroes
#Blog: https://blog.unwiredlearning.com/set-matrix-zeroes