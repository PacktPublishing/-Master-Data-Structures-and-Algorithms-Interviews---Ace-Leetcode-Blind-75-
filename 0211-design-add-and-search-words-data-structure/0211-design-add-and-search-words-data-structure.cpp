
#include <unordered_map>
#include <string>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEnd;

    TrieNode() {
        isEnd = false;
    }
};

class WordDictionary {
private:
    TrieNode* root;

public:
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        return dfs(word, root, 0);
    }

    bool dfs(string word, TrieNode* node, int index) {
        if (index == word.length()) {
            return node->isEnd;
        }

        char c = word[index];
        if (c == '.') {
            for (auto child : node->children) {
                if (dfs(word, child.second, index + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            return node->children.find(c) != node->children.end() && dfs(word, node->children[c], index + 1);
        }
    }
};
