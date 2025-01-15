
#include <iostream>
#include <vector>
#include <algorithm>

int minMeetingRooms(std::vector<std::pair<int, int>> intervals) {
    std::vector<int> start_times, end_times;

    for (const auto& interval : intervals) {
        start_times.push_back(interval.first);
        end_times.push_back(interval.second);
    }

    std::sort(start_times.begin(), start_times.end());
    std::sort(end_times.begin(), end_times.end());

    int start_pointer = 0, end_pointer = 0, used_rooms = 0, max_rooms = 0;

    while (start_pointer < intervals.size()) {
        if (start_times[start_pointer] < end_times[end_pointer]) {
            used_rooms++;
            start_pointer++;
        } else {
            used_rooms--;
            end_pointer++;
        }
        max_rooms = std::max(max_rooms, used_rooms);
    }

    return max_rooms;
}

int main() {
    std::vector<std::pair<int, int>> intervals = {{0, 30}, {5, 10}, {15, 20}};
    std::cout << minMeetingRooms(intervals) << std::endl;
    return 0;
}
