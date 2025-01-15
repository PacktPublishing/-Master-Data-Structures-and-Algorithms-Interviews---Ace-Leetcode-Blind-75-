
class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    isSubtree(root, subRoot) {
        if (subRoot === null) {
            return true;
        }
        if (root === null) {
            return false;
        }
        if (this.isSameTree(root, subRoot)) {
            return true;
        }
        return this.isSubtree(root.left, subRoot) || this.isSubtree(root.right, subRoot);
    }

    isSameTree(p, q) {
        if (p === null && q === null) {
            return true;
        }
        if (p === null || q === null || p.val !== q.val) {
            return false;
        }
        return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right);
    }
}

// Example usage:
// const root = new TreeNode(1);
// const subRoot = new TreeNode(1);
// const solution = new Solution();
// console.log(solution.isSubtree(root, subRoot));
        