class TreeNode {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    kthSmallest(root, k) {
        const ioList = [];
        this.inOrderTraversal(root, ioList);
        return ioList[k - 1];
    }

    inOrderTraversal(node, ioList) {
        if (node === null) {
            return;
        }

        this.inOrderTraversal(node.left, ioList);
        ioList.push(node.val);
        this.inOrderTraversal(node.right, ioList);
    }
}
