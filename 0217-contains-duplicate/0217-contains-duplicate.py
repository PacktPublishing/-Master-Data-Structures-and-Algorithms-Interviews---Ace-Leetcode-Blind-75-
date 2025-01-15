class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique numbers
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        return False


#Question: https://leetcode.com/problems/contains-duplicate
#Blog: https://blog.unwiredlearning.com/contains-duplicate