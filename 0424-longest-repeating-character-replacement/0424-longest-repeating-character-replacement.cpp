#include <unordered_map>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> count;
        int maxLen = 0;
        int left = 0;
        int maxFreq = 0;

        for (int right = 0; right < s.length(); ++right) {
            count[s[right]]++;
            maxFreq = max(maxFreq, count[s[right]]);

            while (right - left + 1 - maxFreq > k) {
                count[s[left]]--;
                left++;
            }

            maxLen = max(maxLen, right - left + 1);
        }

        return maxLen;
    }
};
