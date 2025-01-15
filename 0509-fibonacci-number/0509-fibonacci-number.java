class Solution {
    public int fib(int n) {
        // Base case: if n is 0 or 1, return n directly
        if (n <= 1) {
            return n;
        }

        // Initialize an array (dp) to store computed Fibonacci numbers
        int[] dp = new int[n + 1];

        dp[0] = 0;
        dp[1] = 1;

        // Start calculating Fibonacci numbers from 2 to n
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        // Return the nth Fibonacci number
        return dp[n];
    }
}