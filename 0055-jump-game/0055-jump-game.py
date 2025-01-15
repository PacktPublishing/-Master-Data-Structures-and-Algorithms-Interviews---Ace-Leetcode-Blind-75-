class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # stores the farthest index we can reach
        maxReach = 0
        
        # Iterate through each index in the array
        for i in range(len(nums)):
            # If the current index is greater than the farthest we can reach,
            # it means we cannot reach this index, hence return False
            if i > maxReach:
                return False
            
            # Update maxReach to be the maximum of its current value
            # and the farthest index we can reach from the current index
            maxReach = max(maxReach, i + nums[i])
        
        # If we have iterated through the array and maxReach is at least the last index,
        # it means we can reach the end, hence return True
        result = maxReach >= len(nums) - 1
        return result
    

#Question: https://leetcode.com/problems/jump-game
#Blog: https://blog.unwiredlearning.com/jump-game