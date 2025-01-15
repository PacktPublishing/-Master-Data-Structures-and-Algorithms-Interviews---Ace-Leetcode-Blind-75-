class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize bucket as a list of empty lists
        bucket = [[] for _ in range(len(nums) + 1)]
        frequencyMap = {}

        # Fill frequencyMap
        for n in nums:
            if n not in frequencyMap:
                frequencyMap[n] = 1
            else:
                frequencyMap[n] += 1

        # Fill bucket
        for key, frequency in frequencyMap.items():
            bucket[frequency].append(key)

        result = []
        # Iterate through bucket in reverse to get top k frequent elements
        for i in reversed(range(len(bucket))):
            if bucket[i]:
                for value in bucket[i]:
                    if len(result) < k:
                        result.append(value)
                    else:
                        return result
        return result
    

#Question: https://leetcode.com/problems/top-k-frequent-elements
#Blog: https://blog.unwiredlearning.com/top-k-frequent-elements