#include <string>
#include <unordered_map>
#include <climits>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) return "";

        unordered_map<char, int> dictT;
        for (char c : t) {
            dictT[c]++;
        }

        int required = dictT.size();
        int left = 0, right = 0, formed = 0;
        unordered_map<char, int> windowCounts;
        int minLen = INT_MAX;
        int minLeft = 0, minRight = 0;

        while (right < s.size()) {
            char c = s[right];
            windowCounts[c]++;

            if (dictT.count(c) && windowCounts[c] == dictT[c]) {
                formed++;
            }

            while (left <= right && formed == required) {
                c = s[left];

                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minLeft = left;
                    minRight = right;
                }

                windowCounts[c]--;
                if (dictT.count(c) && windowCounts[c] < dictT[c]) {
                    formed--;
                }

                left++;
            }

            right++;
        }

        return minLen == INT_MAX ? "" : s.substr(minLeft, minRight - minLeft + 1);
    }
};
