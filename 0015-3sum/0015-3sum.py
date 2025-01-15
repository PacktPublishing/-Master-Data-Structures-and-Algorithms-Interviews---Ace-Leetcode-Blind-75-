class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Check if the array is null or has less than 3 elements
        if nums is None or len(nums) < 3:
            return []

        # Sort the elements
        nums.sort()

        # Use a set to keep unique triplets
        result = set()

        # Fix i'th element and find the other two elements
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                target = nums[i] + nums[left] + nums[right]
                
                if target == 0:
                    # Add the triplet to the set
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                
                # If target is less than 0, increment the left pointer
                elif target < 0:
                    left += 1
                
                # If target is greater than 0, decrement the right pointer
                elif target > 0:
                    right -= 1

        # Convert set of tuples to list of lists
        return list(map(list, result))
    

#Question: https://leetcode.com/problems/3sum
#Blog: https://blog.unwiredlearning.com/3sum