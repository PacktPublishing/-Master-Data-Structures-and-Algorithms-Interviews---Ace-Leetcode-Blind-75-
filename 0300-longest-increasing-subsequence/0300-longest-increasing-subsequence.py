class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        dp = [1 for _ in range(len(nums))]
        max_length = 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_length = max(max_length, dp[i])
        
        return max_length
        
        
#Question: https://leetcode.com/problems/longest-increasing-subsequence
#Blog: https://blog.unwiredlearning.com/longest-increasing-subsequence