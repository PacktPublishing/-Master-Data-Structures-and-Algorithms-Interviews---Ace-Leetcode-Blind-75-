class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)
        
        # XOR all indices and all elements in nums
        for i in range(n):
            xor = xor ^ i ^ nums[i]
        
        # Finally XOR with n (since the range is from 0 to n)
        xor = xor ^ n
        
        return xor
    

#Question: https://leetcode.com/problems/missing-number
#Blog: https://blog.unwiredlearning.com/missing-number