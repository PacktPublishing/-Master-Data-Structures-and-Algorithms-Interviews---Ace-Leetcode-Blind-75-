
function longestPalindrome(s) {
    const n = s.length;
    if (n < 2) {
        return s;
    }
    const dp = Array.from({ length: n }, () => Array(n).fill(false));

    // Initialize start position and max length of the palindrome
    let start = 0, maxLength = 1;

    // Base case: single character palindromes
    for (let i = 0; i < n; i++) {
        dp[i][i] = true;
    }

    // Base case: two-character palindromes
    for (let i = 0; i < n - 1; i++) {
        if (s[i] === s[i + 1]) {
            dp[i][i + 1] = true;
            start = i;
            maxLength = 2;
        }
    }

    // General case
    for (let length = 3; length <= n; length++) {
        for (let i = 0; i < n - length + 1; i++) {
            let j = i + length - 1;
            if (s[i] === s[j] && dp[i + 1][j - 1]) {
                dp[i][j] = true;
                start = i;
                maxLength = length;
            }
        }
    }

    return s.substring(start, start + maxLength);
}
