// C++ implementation of group anagrams
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> anagramMap;
    
    for (string word : strs) {
        vector<int> count(26, 0);
        for (char c : word) {
            count[c - 'a']++;
        }
        string key;
        for (int i = 0; i < 26; ++i) {
            key += string(1, count[i] + '0');
        }
        anagramMap[key].push_back(word);
    }
    
    vector<vector<string>> result;
    for (auto& pair : anagramMap) {
        result.push_back(pair.second);
    }
    return result;
}

int main() {
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result = groupAnagrams(strs);
    for (const auto& group : result) {
        for (const auto& word : group) {
            cout << word << " ";
        }
        cout << endl;
    }
    return 0;
}
