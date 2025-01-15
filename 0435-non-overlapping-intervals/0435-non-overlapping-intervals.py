class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by start time
        intervals.sort()
        
        # Initialize the previous interval end time and count
        prev_end = intervals[0][1]
        count = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                # Overlap detected, increment the count
                count += 1
                # Keep the interval with the smaller end to minimize future overlaps
                prev_end = min(prev_end, intervals[i][1])
            else:
                # No overlap, update the prev_end to current interval's end
                prev_end = intervals[i][1]
        
        return count


#Question: https://leetcode.com/problems/non-overlapping-intervals
#Blog: https://blog.unwiredlearning.com/non-overlapping-intervals