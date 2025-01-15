class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int val) {
        this.val = val;
    }
}

public class Solution {
    public boolean isValidBST(TreeNode root) {
        List<Integer> ioList = new ArrayList<>();
        helper(root, ioList);
        
        boolean isBST = true;
        int prev = ioList.get(0);
        
        for (int i = 1; i < ioList.size(); i++) {
            if (ioList.get(i) <= prev) {
                isBST = false;
            }
            prev = ioList.get(i);
        }
        
        return isBST;
    }

    private void helper(TreeNode node, List<Integer> ioList) {
        if (node == null) return;

        helper(node.left, ioList);
        ioList.add(node.val);
        helper(node.right, ioList);
    }
}
