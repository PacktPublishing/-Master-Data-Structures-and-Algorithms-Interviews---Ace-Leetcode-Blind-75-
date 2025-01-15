class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

function invertTree(root) {
    if (root === null) {
        return null;
    }

    // Swap the left and right children
    [root.left, root.right] = [root.right, root.left];

    // Recursively invert the left and right subtree
    invertTree(root.left);
    invertTree(root.right);

    return root;
}