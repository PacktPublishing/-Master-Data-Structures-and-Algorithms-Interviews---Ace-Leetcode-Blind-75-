class TreeNode {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    constructor() {
        this.maxSum = -Infinity;
    }

    maxPathSum(root) {
        this.dfs(root);
        return this.maxSum;
    }

    dfs(node) {
        if (node === null) {
            return 0;
        }

        const leftGain = Math.max(this.dfs(node.left), 0);
        const rightGain = Math.max(this.dfs(node.right), 0);

        const priceNewPath = node.val + leftGain + rightGain;
        this.maxSum = Math.max(this.maxSum, priceNewPath);

        return node.val + Math.max(leftGain, rightGain);
    }
}
