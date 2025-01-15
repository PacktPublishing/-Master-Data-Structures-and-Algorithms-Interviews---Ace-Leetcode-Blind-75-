class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }

        // Create 2 new arrays
        int[] skipLastHouse = new int[nums.length - 1];
        int[] skipFirstHouse = new int[nums.length - 1];
        System.arraycopy(nums, 0, skipLastHouse, 0, nums.length - 1);
        System.arraycopy(nums, 1, skipFirstHouse, 0, nums.length - 1);

        // Get the loot from both possibilities
        int lootSkippingLast = robHelper(skipLastHouse);
        int lootSkippingFirst = robHelper(skipFirstHouse);

        // Return the maximum of 2 loots
        return Math.max(lootSkippingLast, lootSkippingFirst);
    }

    private int robHelper(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }

        return dp[nums.length - 1];
    }
}

//Question: https://leetcode.com/problems/house-robber-ii
//Blog: https://blog.unwiredlearning.com/house-robber-ii
