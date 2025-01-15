class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0            
        if len(nums) == 1:
            return nums[0]

        # Create 2 new lists
        skip_last_house = nums[:-1]
        skip_first_house = nums[1:]

        # Get the loot from both possibilities
        loot_skipping_last = self.rob_helper(skip_last_house)
        loot_skipping_first = self.rob_helper(skip_first_house)

        # Return the maximum of 2 loots
        return max(loot_skipping_last, loot_skipping_first)

    def rob_helper(self, nums):
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]
        
        
#Question: https://leetcode.com/problems/house-robber-ii
#Blog: https://blog.unwiredlearning.com/house-robber-ii