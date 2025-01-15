#include <algorithm>
#include <climits>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int maxSum = INT_MIN;
        dfs(root, maxSum);
        return maxSum;
    }

private:
    int dfs(TreeNode* node, int& maxSum) {
        if (node == nullptr) {
            return 0;
        }

        int leftGain = std::max(dfs(node->left, maxSum), 0);
        int rightGain = std::max(dfs(node->right, maxSum), 0);

        int priceNewPath = node->val + leftGain + rightGain;
        maxSum = std::max(maxSum, priceNewPath);

        return node->val + std::max(leftGain, rightGain);
    }
};
