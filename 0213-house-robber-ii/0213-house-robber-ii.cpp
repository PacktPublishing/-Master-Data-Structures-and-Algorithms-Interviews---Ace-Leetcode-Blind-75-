#include <vector>
#include <algorithm>

class Solution {
public:
    int rob(std::vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }

        // Create 2 new vectors
        std::vector<int> skipLastHouse(nums.begin(), nums.end() - 1);
        std::vector<int> skipFirstHouse(nums.begin() + 1, nums.end());

        // Get the loot from both possibilities
        int lootSkippingLast = robHelper(skipLastHouse);
        int lootSkippingFirst = robHelper(skipFirstHouse);

        // Return the maximum of 2 loots
        return std::max(lootSkippingLast, lootSkippingFirst);
    }

private:
    int robHelper(const std::vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        std::vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = std::max(nums[0], nums[1]);

        for (size_t i = 2; i < nums.size(); i++) {
            dp[i] = std::max(dp[i - 2] + nums[i], dp[i - 1]);
        }

        return dp.back();
    }
};

//Question: https://leetcode.com/problems/house-robber-ii
//Blog: https://blog.unwiredlearning.com/house-robber-ii
