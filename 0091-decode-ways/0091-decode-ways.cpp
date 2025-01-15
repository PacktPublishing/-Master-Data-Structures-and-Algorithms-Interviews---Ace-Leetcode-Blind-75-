
#include <string>
#include <vector>

class Solution {
public:
    int numDecodings(const std::string &s) {
        if (s.empty() || s[0] == '0') {
            return 0;
        }

        int n = s.length();
        std::vector<int> dp(n + 1, 0);

        // Base cases
        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            // Single digit decode
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // Two digit decode
            int twoDigit = std::stoi(s.substr(i - 2, 2));
            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] += dp[i - 2];
            }
        }

        return dp[n];
    }
};
