class TreeNode {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    levelOrder(root) {
        if (!root) {
            return [];
        }

        const result = [];
        const queue = [root];

        while (queue.length > 0) {
            const levelSize = queue.length;
            const level = [];

            for (let i = 0; i < levelSize; i++) {
                const node = queue.shift();
                level.push(node.val);
                if (node.left) {
                    queue.push(node.left);
                }
                if (node.right) {
                    queue.push(node.right);
                }
            }

            result.push(level);
        }

        return result;
    }
}
