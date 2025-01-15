class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # Initialize the DP table with False.
        dp = [[False] * n for _ in range(n)]
        count = 0

        # Base case: single characters
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Base case: two consecutive characters
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1

        # DP case: substrings of length 3 to n
        for length in range(3, n+1):

            # Iterate through all starting indices for the current length.
            for i in range(n-length+1):

                # Calculate the ending index of the current substring.
                j = i+length-1

                # Check if the current substring is a palindrome.
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1

        return count


#Question: https://leetcode.com/problems/palindromic-substrings
#Blog: https://blog.unwiredlearning.com/palindromic-substrings