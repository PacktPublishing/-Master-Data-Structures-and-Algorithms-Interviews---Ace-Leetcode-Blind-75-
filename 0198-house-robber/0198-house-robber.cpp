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
        
        std::vector<int> dp(nums.size());
        dp[0] = nums[0];
        dp[1] = std::max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.size(); ++i) {
            dp[i] = std::max(dp[i - 2] + nums[i], dp[i - 1]);
        }
        
        return dp.back();
    }
};