class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the pointers for the start and end of the array
        left, right = 0, len(nums) - 1
        
        # Continue searching while the search space is valid
        while left <= right:
            # Calculate the middle index of the current search space
            # Using left + (right - left) // 2 to avoid integer overflow
            mid = left + (right - left) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid  # Target found, return its index
            elif nums[mid] > target:
                # If the middle element is greater than the target,
                # narrow the search to the left half of the array
                right = mid - 1
            else:
                # If the middle element is less than the target,
                # narrow the search to the right half of the array
                left = mid + 1
        
        # Target not found in the array, return -1
        return -1
    

#Question: https://leetcode.com/problems/binary-search
#Blog: https://blog.unwiredlearning.com/binary-search