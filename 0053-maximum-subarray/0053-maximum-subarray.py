class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # the sum of the subarray ending at the current index
        current_sum = nums[0]
        
        # This will store the maximum sum found so far
        max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Update current_sum to be the maximum of:
            # 1. The current element itself (which means starting a new subarray)
            # 2. The current element + current_sum (which means extending the existing subarray)
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update max_sum to be the maximum of max_sum and current_sum
            # This ensures max_sum always holds the highest sum encountered
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum sum found
        return max_sum
    
    
#Question: https://leetcode.com/problems/maximum-subarray
#Blog: https://blog.unwiredlearning.com/maximum-subarray