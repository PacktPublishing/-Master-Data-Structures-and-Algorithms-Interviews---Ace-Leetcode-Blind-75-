#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while (root != nullptr) {
            // If both p and q are greater than root, go to right subtree
            if (p->val > root->val && q->val > root->val) {
                root = root->right;
            }
            // If both p and q are lesser than root, go to left subtree
            else if (p->val < root->val && q->val < root->val) {
                root = root->left;
            } else {
                // We have found the split point, i.e. the LCA node.
                return root;
            }
        }
        return nullptr;
    }
};
