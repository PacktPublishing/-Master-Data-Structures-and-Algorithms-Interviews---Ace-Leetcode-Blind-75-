class TreeNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Solution {
    buildTree(preorder, inorder) {
        // Create a map to efficiently find the index of any element in inorder list
        const io_map = new Map();
        for (let i = 0; i < inorder.length; i++) {
            io_map.set(inorder[i], i);
        }
        
        // Call recursive helper function to build the tree
        return this.splitTree(preorder, io_map, 0, 0, inorder.length - 1);
    }

    splitTree(preorder, io_map, rootIndex, left, right) {
        // Base case: if the left index exceeds the right index, subtree is empty
        if (left > right) {
            return null;
        }
        
        // Create the root node with the current root element
        const root = new TreeNode(preorder[rootIndex]);
        
        // Find the index of the root element in inorder list
        const mid = io_map.get(preorder[rootIndex]);
        
        // Recursively build the left subtree
        if (mid > left) {
            root.left = this.splitTree(preorder, io_map, rootIndex + 1, left, mid - 1);
        }
        
        // Recursively build the right subtree
        if (mid < right) {
            root.right = this.splitTree(preorder, io_map, rootIndex + mid - left + 1, mid + 1, right);
        }
        
        return root;
    }
}

// Example usage
// const solution = new Solution();
// const tree = solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]);
