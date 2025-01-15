class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:   
        
        # Initialize the boundaries
        rowBegin, rowEnd = 0, len(matrix) - 1
        colBegin, colEnd = 0, len(matrix[0]) - 1
        
        # Resultant list
        result = []
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # colBegin to colEnd along the rowBegin boundary
            for i in range(colBegin, colEnd + 1):
                result.append(matrix[rowBegin][i])
            rowBegin += 1
            
            # rowBegin to rowEnd along the colEnd boundary
            for i in range(rowBegin, rowEnd + 1):
                result.append(matrix[i][colEnd])
            colEnd -= 1
            
            if rowBegin <= rowEnd:
                # colEnd to colBegin along the rowEnd boundary
                for i in range(colEnd, colBegin - 1, -1):
                    result.append(matrix[rowEnd][i])
                rowEnd -= 1
            
            if colBegin <= colEnd:
                # rowEnd to rowBegin along the colBegin boundary
                for i in range(rowEnd, rowBegin - 1, -1):
                    result.append(matrix[i][colBegin])
                colBegin += 1
        
        return result
    

#Question: https://leetcode.com/problems/spiral-matrix
#Blog: https://blog.unwiredlearning.com/spiral-matrix