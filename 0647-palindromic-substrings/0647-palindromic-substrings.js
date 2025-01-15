class Solution {
    countSubstrings(s) {
        const n = s.length;

        // Initialize the DP table with false.
        const dp = Array.from({ length: n }, () => Array(n).fill(false));
        let count = 0;

        // Base case: single characters
        for (let i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }

        // Base case: two consecutive characters
        for (let i = 0; i < n - 1; i++) {
            if (s[i] === s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }

        // DP case: substrings of length 3 to n
        for (let length = 3; length <= n; length++) {
            for (let i = 0; i <= n - length; i++) {
                const j = i + length - 1;

                if (s[i] === s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    count++;
                }
            }
        }

        return count;
    }
}

//Question: https://leetcode.com/problems/palindromic-substrings
//Blog: https://blog.unwiredlearning.com/palindromic-substrings
