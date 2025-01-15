class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i
      
            
#Question: https://leetcode.com/problems/two-sum
#Blog: https://blog.unwiredlearning.com/two-sum