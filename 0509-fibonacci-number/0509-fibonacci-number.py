class Solution:
    def fib(self, n: int) -> int:
        # Base case: if n is 0 or 1, return n directly
        if n <= 1:
            return n

        # Initialize a list (dp) to store computed Fibonacci numbers
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 1

        # Start calculating Fibonacci numbers from 2 to n
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        # Return the nth Fibonacci number
        return dp[n]
    
    
#Question: https://leetcode.com/problems/fibonacci-number
#Blog: https://blog.unwiredlearning.com/fibonacci-number