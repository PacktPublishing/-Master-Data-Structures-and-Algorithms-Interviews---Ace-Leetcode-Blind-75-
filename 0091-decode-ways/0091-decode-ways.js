
function numDecodings(s) {
    if (!s || s[0] === '0') {
        return 0;
    }

    const n = s.length;
    const dp = new Array(n + 1).fill(0);

    // Base cases
    dp[0] = 1;
    dp[1] = 1;

    for (let i = 2; i <= n; i++) {
        // Single digit decode
        if (s[i - 1] !== '0') {
            dp[i] += dp[i - 1];
        }
        // Two digit decode
        const twoDigit = parseInt(s.substring(i - 2, i), 10);
        if (twoDigit >= 10 && twoDigit <= 26) {
            dp[i] += dp[i - 2];
        }
    }

    return dp[n];
}
