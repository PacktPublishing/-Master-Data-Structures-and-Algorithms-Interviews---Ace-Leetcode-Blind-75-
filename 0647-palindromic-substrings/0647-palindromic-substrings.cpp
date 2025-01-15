#include <vector>
#include <string>

class Solution {
public:
    int countSubstrings(const std::string& s) {
        int n = s.length();

        // Initialize the DP table with false.
        std::vector<std::vector<bool>> dp(n, std::vector<bool>(n, false));
        int count = 0;

        // Base case: single characters
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }

        // Base case: two consecutive characters
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }

        // DP case: substrings of length 3 to n
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;

                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    count++;
                }
            }
        }

        return count;
    }
};

//Question: https://leetcode.com/problems/palindromic-substrings
//Blog: https://blog.unwiredlearning.com/palindromic-substrings
