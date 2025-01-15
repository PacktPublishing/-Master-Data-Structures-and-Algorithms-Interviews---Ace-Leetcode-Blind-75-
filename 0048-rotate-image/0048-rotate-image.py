class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Iterate over each layer of the matrix
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                # Save the temp element
                temp = matrix[i][j]

                # Move bottom-left element to top-left
                matrix[i][j] = matrix[n - j - 1][i]

                # Move bottom-right element to bottom-left
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]

                # Move top-right element to bottom-right
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

                # Assign temp element to top-right
                matrix[j][n - i - 1] = temp


#Question: https://leetcode.com/problems/rotate-image
#Blog: https://blog.unwiredlearning.com/rotate-image