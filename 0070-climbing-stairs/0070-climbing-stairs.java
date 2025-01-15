class Solution {
    public int climbStairs(int n) {
        // Base case: if n is 1, there's only one way.
        if (n == 1) {
            return n;
        }
        
        // Initialize an array to store the number of ways to reach each step.
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        
        // Start calculating from the 3rd step up to the nth step.
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // dp[n] contains the total number of ways to climb n stairs.
        return dp[n];
    }
}