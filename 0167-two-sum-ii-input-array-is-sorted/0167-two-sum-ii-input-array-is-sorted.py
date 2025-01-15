class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: left at the start, right at the end.
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            # Return the 1-indexed positions if the target sum is found.
            if current_sum == target:
                return [left + 1, right + 1]  
            
            # Move the left pointer to the right if the sum is less than the target.
            elif current_sum < target:
                left += 1
            
            # Move the right pointer to the left if the sum is greater than the target.
            elif current_sum > target:
                right -= 1

        return []
    

#Question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
#Blog: https://blog.unwiredlearning.com/two-sum-ii-input-array-is-sorted