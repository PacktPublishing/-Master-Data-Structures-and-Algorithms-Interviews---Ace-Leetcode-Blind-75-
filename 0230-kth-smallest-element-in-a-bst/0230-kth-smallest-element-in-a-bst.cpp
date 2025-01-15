#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        std::vector<int> ioList;
        inOrderTraversal(root, ioList);
        return ioList[k - 1];
    }

private:
    void inOrderTraversal(TreeNode* node, std::vector<int>& ioList) {
        if (node == nullptr) {
            return;
        }

        inOrderTraversal(node->left, ioList);
        ioList.push_back(node->val);
        inOrderTraversal(node->right, ioList);
    }
};
