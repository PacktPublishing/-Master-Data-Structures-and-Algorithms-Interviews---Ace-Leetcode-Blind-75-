
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
#include <stack>

using namespace std;

class AlienDictionary {
public:
    string alienOrder(vector<string>& words) {
        // Step 1: Create the graph.
        unordered_map<char, unordered_set<char>> adj;
        for (const string& word : words) {
            for (char c : word) {
                adj[c];
            }
        }

        for (int i = 0; i < words.size() - 1; i++) {
            string word1 = words[i];
            string word2 = words[i + 1];
            int minLen = min(word1.size(), word2.size());

            // Handle the case where order is impossible.
            if (word1.size() > word2.size() && word1.substr(0, minLen) == word2.substr(0, minLen)) {
                return "";
            }

            for (int j = 0; j < minLen; j++) {
                if (word1[j] != word2[j]) {
                    adj[word1[j]].insert(word2[j]);
                    break;
                }
            }
        }

        // Step 2: Detect cycles and perform DFS.
        unordered_map<char, bool> visited; // false = visited but not processed, true = processed
        vector<char> order;

        for (const auto& pair : adj) {
            if (visited.find(pair.first) == visited.end()) {
                if (!dfs(pair.first, adj, visited, order)) {
                    return ""; // Cycle detected.
                }
            }
        }

        // Reverse the post-visit ordered list.
        reverse(order.begin(), order.end());
        return string(order.begin(), order.end());
    }

private:
    bool dfs(char c, unordered_map<char, unordered_set<char>>& adj, unordered_map<char, bool>& visited, vector<char>& order) {
        if (visited.find(c) != visited.end()) {
            return visited[c]; // If true, no cycle; if false, cycle detected.
        }
        visited[c] = false;
        for (char neighbor : adj[c]) {
            if (!dfs(neighbor, adj, visited, order)) {
                return false; // Cycle detected.
            }
        }
        visited[c] = true;
        order.push_back(c);
        return true;
    }
};
