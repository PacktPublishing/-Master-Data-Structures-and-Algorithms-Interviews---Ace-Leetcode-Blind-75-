class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:        
        # Sum for starting window
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]

        max_sum = current_sum
        
        # Start sliding window
        start_index = 0
        end_index = k
        
        while end_index < len(nums):

            # Remove previous element
            current_sum -= nums[start_index]  
            start_index += 1
            
            # Add next element
            current_sum += nums[end_index]  
            end_index += 1
            
            # Update max sum
            max_sum = max(max_sum, current_sum)  
            
        # Return the average
        return max_sum / k
    

#Question: https://leetcode.com/problems/maximum-average-subarray-i
#Blog: https://blog.unwiredlearning.com/maximum-average-subarray-i