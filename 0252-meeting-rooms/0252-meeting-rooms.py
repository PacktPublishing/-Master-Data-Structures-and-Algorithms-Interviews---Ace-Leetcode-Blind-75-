def can_attend_meetings(intervals):
    intervals.sort()
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
        
    return True


#Question: https://www.lintcode.com/problem/920/
#Blog: https://blog.unwiredlearning.com/meeting-rooms