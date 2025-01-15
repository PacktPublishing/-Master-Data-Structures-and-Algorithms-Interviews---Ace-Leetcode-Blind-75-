class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    lowestCommonAncestor(root, p, q) {
        while (root !== null) {
            // If both p and q are greater than root, go to right subtree
            if (p.val > root.val && q.val > root.val) {
                root = root.right;
            }
            // If both p and q are lesser than root, go to left subtree
            else if (p.val < root.val && q.val < root.val) {
                root = root.left;
            } else {
                // We have found the split point, i.e. the LCA node.
                return root;
            }
        }
        return null;
    }
}
