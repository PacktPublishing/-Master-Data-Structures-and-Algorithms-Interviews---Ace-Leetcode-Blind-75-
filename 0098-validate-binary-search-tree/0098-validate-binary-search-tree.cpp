#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        vector<int> ioList;
        helper(root, ioList);

        bool isBST = true;
        int prev = ioList[0];

        for (int i = 1; i < ioList.size(); i++) {
            if (ioList[i] <= prev) {
                isBST = false;
            }
            prev = ioList[i];
        }

        return isBST;
    }

private:
    void helper(TreeNode* node, vector<int>& ioList) {
        if (node == nullptr) return;

        helper(node->left, ioList);
        ioList.push_back(node->val);
        helper(node->right, ioList);
    }
};
