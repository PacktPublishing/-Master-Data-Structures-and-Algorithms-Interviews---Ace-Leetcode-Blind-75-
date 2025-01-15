def minMeetingRooms(intervals):
    # Separate and sort start and end times
    start_times = sorted(interval.start for interval in intervals)
    end_times = sorted(interval.end for interval in intervals)

    start_pointer, end_pointer = 0, 0
    used_rooms = 0
    max_rooms = 0

    # Iterate over start times
    while start_pointer < len(intervals):
        if start_times[start_pointer] < end_times[end_pointer]:
            # A new room is needed
            used_rooms += 1
            start_pointer += 1
        else:
            # A room is freed up
            used_rooms -= 1
            end_pointer += 1
        
        # Update the maximum number of rooms needed
        max_rooms = max(max_rooms, used_rooms)

    return max_rooms


#Question: https://www.lintcode.com/problem/919/
#Blog: https://blog.unwiredlearning.com/meeting-rooms-ii