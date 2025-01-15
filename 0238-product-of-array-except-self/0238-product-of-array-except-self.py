class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Array to store all left multiplication
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Array to store all right multiplication
        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        result = [1] * n
        for i in range(n):
            result[i] = left[i] * right[i]

        return result 
    

#Question: https://leetcode.com/problems/product-of-array-except-self
#Blog: https://blog.unwiredlearning.com/product-of-array-except-self