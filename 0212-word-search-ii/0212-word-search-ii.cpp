
#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>

using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = buildTrie(words);
        unordered_set<string> result;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (root->children.count(board[i][j])) {
                    dfs(board, root, i, j, "", result);
                }
            }
        }
        return vector<string>(result.begin(), result.end());
    }

private:
    TrieNode* buildTrie(vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (string word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->isEnd = true;
        }
        return root;
    }

    void dfs(vector<vector<char>>& board, TrieNode* node, int i, int j, string path, unordered_set<string>& result) {
        if (node->isEnd) {
            result.insert(path);
            node->isEnd = false; // Avoid duplicates
        }
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || !node->children.count(board[i][j])) {
            return;
        }
        char temp = board[i][j];
        board[i][j] = '#'; // Mark as visited
        for (pair<int, int> dir : {pair<int, int>{0, 1}, {1, 0}, {0, -1}, {-1, 0}}) {
            int x = i + dir.first, y = j + dir.second;
            dfs(board, node->children[temp], x, y, path + temp, result);
        }
        board[i][j] = temp; // Unmark
    }
};
