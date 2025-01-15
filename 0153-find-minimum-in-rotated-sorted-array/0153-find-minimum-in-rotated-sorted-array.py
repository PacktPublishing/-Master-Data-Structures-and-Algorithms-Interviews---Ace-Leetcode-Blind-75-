class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If the middle element is greater than the rightmost element, 
            # it indicates that the smallest element is in the right half.
            # Thus, adjust the left pointer to mid + 1.
            if nums[mid] > nums[right]:
                left = mid + 1
            
            # If the middle element is greater than the rightmost element, 
            # it indicates that the smallest element is in the right half.
            # Thus, adjust the left pointer to mid + 1.
            else:
                right = mid

        # At the end of the loop, left will be pointing at the smallest element.        
        return nums[left]
        
        
#Question: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
#Blog: https://blog.unwiredlearning.com/find-minimum-in-rotated-sorted-array