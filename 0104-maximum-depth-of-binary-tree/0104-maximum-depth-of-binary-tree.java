
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int maxDepth = 0;
        Stack<TreeNodeDepthPair> stack = new Stack<>();
        stack.push(new TreeNodeDepthPair(root, 1));

        while (!stack.isEmpty()) {
            TreeNodeDepthPair current = stack.pop();
            TreeNode node = current.node;
            int depth = current.depth;

            if (node != null) {
                maxDepth = Math.max(maxDepth, depth);
                if (node.left != null) {
                    stack.push(new TreeNodeDepthPair(node.left, depth + 1));
                }
                if (node.right != null) {
                    stack.push(new TreeNodeDepthPair(node.right, depth + 1));
                }
            }
        }

        return maxDepth;
    }

    private class TreeNodeDepthPair {
        TreeNode node;
        int depth;

        TreeNodeDepthPair(TreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }
}
