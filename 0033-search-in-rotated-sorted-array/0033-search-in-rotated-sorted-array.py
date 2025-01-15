class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1

        # Iterate as long as left is less than or equal to right
        while left <= right:
            # Calculate mid to avoid overflow
            mid = left + (right - left) // 2

            # Check if the mid element is the target
            if nums[mid] == target:
                return mid  # Target found

            # If the left half is sorted
            if nums[mid] >= nums[left]:
                # Check if target lies in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Narrow down to left half
                else:
                    left = mid + 1  # Narrow down to right half

            # If the right half is sorted
            else:                
                # Check if target lies in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Narrow down to right half
                else:
                    right = mid - 1  # Narrow down to left half

        # Target not found
        return -1


#Question: https://leetcode.com/problems/search-in-rotated-sorted-array
#Blog: https://blog.unwiredlearning.com/search-in-rotated-sorted-array