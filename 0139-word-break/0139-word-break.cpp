#include <vector>
#include <string>
#include <unordered_set>

class Solution {
public:
    bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        std::unordered_set<std::string> wordSet(wordDict.begin(), wordDict.end());
        std::vector<bool> res(s.length() + 1, false);
        res[0] = true;

        for (int i = 0; i <= s.length(); i++) {
            for (const std::string& word : wordSet) {
                if (res[i] && i + word.length() <= s.length() && s.substr(i, word.length()) == word) {
                    res[i + word.length()] = true;
                }
            }
        }

        return res[s.length()];
    }
};
