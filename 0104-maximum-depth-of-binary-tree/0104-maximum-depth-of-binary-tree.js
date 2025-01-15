
class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

function maxDepth(root) {
    if (root === null) {
        return 0;
    }

    let maxDepth = 0;
    const stack = [{ node: root, depth: 1 }];

    while (stack.length > 0) {
        const { node, depth } = stack.pop();

        if (node) {
            maxDepth = Math.max(maxDepth, depth);
            if (node.left) {
                stack.push({ node: node.left, depth: depth + 1 });
            }
            if (node.right) {
                stack.push({ node: node.right, depth: depth + 1 });
            }
        }
    }

    return maxDepth;
}
