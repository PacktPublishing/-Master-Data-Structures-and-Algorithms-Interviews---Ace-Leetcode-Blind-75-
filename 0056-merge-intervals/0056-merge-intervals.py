class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Step 1: Sort the intervals by the start time
        intervals.sort()

        # Step 2: Initialize the result array with the first interval
        merged = [intervals[0]]

        # Step 3: Iterate over the intervals and merge when necessary
        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged
    

#Question: https://leetcode.com/problems/merge-intervals
#Blog: https://blog.unwiredlearning.com/merge-intervals