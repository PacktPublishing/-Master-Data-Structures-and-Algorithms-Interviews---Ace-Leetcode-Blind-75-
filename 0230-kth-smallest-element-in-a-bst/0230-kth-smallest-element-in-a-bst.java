import java.util.*;

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

class Solution {
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> ioList = new ArrayList<>();
        inOrderTraversal(root, ioList);
        return ioList.get(k - 1);
    }

    private void inOrderTraversal(TreeNode node, List<Integer> ioList) {
        if (node == null) {
            return;
        }

        inOrderTraversal(node.left, ioList);
        ioList.add(node.val);
        inOrderTraversal(node.right, ioList);
    }
}
