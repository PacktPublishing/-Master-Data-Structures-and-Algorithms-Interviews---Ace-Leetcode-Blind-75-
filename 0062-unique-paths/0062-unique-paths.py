class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Step 1 and 2: Initialize DP array with 1s
        dp = [[1]*n for _ in range(m)]  
    
        # Step 2: Fill in the dp with unique paths to each cell
        for i in range(1, m):          
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Step 3: Return the result from the bottom-right cell
        return dp[m-1][n-1]
        
        
#Question: https://leetcode.com/problems/unique-paths
#Blog: https://blog.unwiredlearning.com/unique-paths