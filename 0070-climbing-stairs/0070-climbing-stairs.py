class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case: if n is 1, there's only one way.
        if n == 1:
            return n
        
        # Initialize a list to store the number of ways to reach each step.
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        
        # Start calculating from the 3rd step up to the nth step.
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        # dp[n] contains the total number of ways to climb n stairs.
        return dp[n]
    

#Question: https://leetcode.com/problems/climbing-stairs
#Blog: https://blog.unwiredlearning.com/climbing-stairs