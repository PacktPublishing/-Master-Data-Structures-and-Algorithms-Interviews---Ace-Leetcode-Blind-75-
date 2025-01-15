
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if (n < 2) {
            return s;
        }
        vector<vector<bool>> dp(n, vector<bool>(n, false));

        // Initialize start position and max length of the palindrome
        int start = 0, maxLength = 1;

        // Base case: single character palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }

        // Base case: two-character palindromes
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                start = i;
                maxLength = 2;
            }
        }

        // General case
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    start = i;
                    maxLength = length;
                }
            }
        }

        return s.substr(start, maxLength);
    }
};
