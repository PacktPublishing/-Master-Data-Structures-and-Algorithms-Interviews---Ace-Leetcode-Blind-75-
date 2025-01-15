import java.util.HashMap;
import java.util.Map;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // Create a map to efficiently find the index of any element in inorder list
        Map<Integer, Integer> io_map = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            io_map.put(inorder[i], i);
        }
        
        // Call recursive helper function to build the tree
        return splitTree(preorder, io_map, 0, 0, inorder.length - 1);
    }

    private TreeNode splitTree(int[] preorder, Map<Integer, Integer> io_map, int rootIndex, int left, int right) {
        // Base case: if the left index exceeds the right index, subtree is empty
        if (left > right) {
            return null;
        }
        
        // Create the root node with the current root element
        TreeNode root = new TreeNode(preorder[rootIndex]);
        
        // Find the index of the root element in inorder list
        int mid = io_map.get(preorder[rootIndex]);
        
        // Recursively build the left subtree
        if (mid > left) {
            root.left = splitTree(preorder, io_map, rootIndex + 1, left, mid - 1);
        }
        
        // Recursively build the right subtree
        if (mid < right) {
            root.right = splitTree(preorder, io_map, rootIndex + mid - left + 1, mid + 1, right);
        }
        
        return root;
    }
}
