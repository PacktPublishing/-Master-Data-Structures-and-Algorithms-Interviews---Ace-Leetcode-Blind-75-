class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left_product, right_product = 1, 1
        result = nums[0]

        for i in range(n):
            # if any of left or right product become 0, update it to 1
            if left_product == 0: 
                left_product = 1
            if right_product == 0: 
                right_product = 1

            # prefix product
            left_product *= nums[i]

            # suffix product
            right_product *= nums[n - 1 - i]

            result = max(ans, max(left_product, right_product))

        return result
        
        
#Question: https://leetcode.com/problems/maximum-product-subarray
#Blog: https://blog.unwiredlearning.com/maximum-product-subarray