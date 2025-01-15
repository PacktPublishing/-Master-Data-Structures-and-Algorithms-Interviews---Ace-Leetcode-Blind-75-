class Solution:
    def maxArea(self, height: List[int]) -> int: 
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        # Loop until the left pointer is less than the right pointer
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxArea = max(area, maxArea)
            
            # Move the pointer pointing to the shorter height towards the middle
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
    

#Question: https://leetcode.com/problems/container-with-most-water
#Blog: https://blog.unwiredlearning.com/container-with-most-water