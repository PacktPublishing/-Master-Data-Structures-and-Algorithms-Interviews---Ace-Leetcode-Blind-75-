
function minMeetingRooms(intervals) {
    let start_times = intervals.map(interval => interval[0]);
    let end_times = intervals.map(interval => interval[1]);

    start_times.sort((a, b) => a - b);
    end_times.sort((a, b) => a - b);

    let start_pointer = 0, end_pointer = 0, used_rooms = 0, max_rooms = 0;

    while (start_pointer < intervals.length) {
        if (start_times[start_pointer] < end_times[end_pointer]) {
            used_rooms++;
            start_pointer++;
        } else {
            used_rooms--;
            end_pointer++;
        }
        max_rooms = Math.max(max_rooms, used_rooms);
    }

    return max_rooms;
}

// Example usage:
let intervals = [[0, 30], [5, 10], [15, 20]];
console.log(minMeetingRooms(intervals));
