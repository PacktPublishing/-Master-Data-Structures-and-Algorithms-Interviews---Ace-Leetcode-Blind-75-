
#include <stack>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }

        int maxDepth = 0;
        std::stack<std::pair<TreeNode*, int>> stack;
        stack.push({root, 1});

        while (!stack.empty()) {
            auto [node, depth] = stack.top();
            stack.pop();

            if (node) {
                maxDepth = std::max(maxDepth, depth);
                if (node->left) {
                    stack.push({node->left, depth + 1});
                }
                if (node->right) {
                    stack.push({node->right, depth + 1});
                }
            }
        }

        return maxDepth;
    }
};
