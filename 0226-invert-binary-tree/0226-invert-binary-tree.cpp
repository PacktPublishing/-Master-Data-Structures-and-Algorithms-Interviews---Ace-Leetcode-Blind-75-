#include <iostream>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }

        // Swap the left and right children
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;

        // Recursively invert the left and right subtree
        invertTree(root->left);
        invertTree(root->right);

        return root;
    }
};