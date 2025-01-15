class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        # Base cases
        dp[0], dp[1] = 1, 1  

        for i in range(2, n + 1):
            # Single digit decodec
            if 1 <= int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]

            # Two digit decode
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[n]
    
    
#Question: https://leetcode.com/problems/decode-ways
#Blog: https://blog.unwiredlearning.com/decode-ways