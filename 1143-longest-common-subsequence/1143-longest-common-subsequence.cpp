#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    int longestCommonSubsequence(std::string text1, std::string text2) {
        int m = text1.size();
        int n = text2.size();
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

        for (int j = 1; j <= n; ++j) {
            for (int i = 1; i <= m; ++i) {
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = std::max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }

        // The bottom-right corner is the length of the LCS
        return dp[m][n];
    }
};
