class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_length = 0
        hashmap = {}

        # Populate the map with all numbers and mark them as not traveled
        for num in nums:
            hashmap[num] = False

        for num in nums:
            current_length = 1

            # Check in forward direction
            next_num = num + 1
            while next_num in hashmap and not hashmap[next_num]:
                current_length += 1
                hashmap[next_num] = True
                next_num += 1

            # Check in reverse direction
            prev_num = num - 1
            while prev_num in hashmap and not hashmap[prev_num]:
                current_length += 1
                hashmap[prev_num] = True
                prev_num -= 1

            longest_length = max(longest_length, current_length)

        return longest_length


#Question: https://leetcode.com/problems/longest-consecutive-sequence/
#Blog: https://blog.unwiredlearning.com/longest-consecutive-sequence/