class Solution {
    rob(nums) {
        if (!nums || nums.length === 0) {
            return 0;
        }
        if (nums.length === 1) {
            return nums[0];
        }

        // Create 2 new arrays
        const skipLastHouse = nums.slice(0, nums.length - 1);
        const skipFirstHouse = nums.slice(1);

        // Get the loot from both possibilities
        const lootSkippingLast = this.robHelper(skipLastHouse);
        const lootSkippingFirst = this.robHelper(skipFirstHouse);

        // Return the maximum of 2 loots
        return Math.max(lootSkippingLast, lootSkippingFirst);
    }

    robHelper(nums) {
        if (nums.length === 1) {
            return nums[0];
        }

        const dp = new Array(nums.length).fill(0);
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for (let i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
        }

        return dp[nums.length - 1];
    }
}

//Question: https://leetcode.com/problems/house-robber-ii
//Blog: https://blog.unwiredlearning.com/house-robber-ii
