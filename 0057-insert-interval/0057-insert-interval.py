class Solution:
    def insert(self, intervals, newInterval) -> List[List[int]]:
        left, right = [], []
        start, end = newInterval

        for i in intervals:
            # i ends before new_interval starts
            if i[1] < start:  
                left.append(i)

            # i starts after new_interval ends
            elif i[0] > end:  
                right.append(i)

            # i overlaps with new_interval
            else:  
                start = min(start, i[0])
                end = max(end, i[1])

        return left + [[start, end]] + right


#Question: https://leetcode.com/problems/insert-interval
#Blog: https://blog.unwiredlearning.com/insert-interval