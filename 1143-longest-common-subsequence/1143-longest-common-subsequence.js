class Solution {
    longestCommonSubsequence(text1, text2) {
        const m = text1.length;
        const n = text2.length;
        const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));

        for (let j = 1; j <= n; j++) {
            for (let i = 1; i <= m; i++) {
                if (text1[i - 1] === text2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }

        // The bottom-right corner is the length of the LCS
        return dp[m][n];
    }
}
