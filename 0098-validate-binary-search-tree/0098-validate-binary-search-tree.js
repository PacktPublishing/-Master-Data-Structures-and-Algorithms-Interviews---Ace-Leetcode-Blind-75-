class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    isValidBST(root) {
        let ioList = [];
        this.helper(root, ioList);

        let isBST = true;
        let prev = ioList[0];

        for (let i = 1; i < ioList.length; i++) {
            if (ioList[i] <= prev) {
                isBST = false;
            }
            prev = ioList[i];
        }

        return isBST;
    }

    helper(node, ioList) {
        if (node === null) return;

        this.helper(node.left, ioList);
        ioList.push(node.val);
        this.helper(node.right, ioList);
    }
}
