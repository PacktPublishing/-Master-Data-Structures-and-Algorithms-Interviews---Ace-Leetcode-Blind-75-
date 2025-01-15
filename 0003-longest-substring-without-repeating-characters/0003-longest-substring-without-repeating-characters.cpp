#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> charIndexMap;
        int maxLength = 0, left = 0;

        for (int right = 0; right < s.length(); ++right) {
            char currentChar = s[right];
            if (charIndexMap.find(currentChar) != charIndexMap.end() && charIndexMap[currentChar] >= left) {
                left = charIndexMap[currentChar] + 1;
            }
            charIndexMap[currentChar] = right;
            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};
