
#include <iostream>
#include <vector>
#include <algorithm>

bool canAttendMeetings(std::vector<std::pair<int, int>> intervals) {
    std::sort(intervals.begin(), intervals.end());
    
    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i].first < intervals[i - 1].second) {
            return false;
        }
    }

    return true;
}

int main() {
    std::vector<std::pair<int, int>> intervals = {{0, 30}, {5, 10}, {15, 20}};
    std::cout << (canAttendMeetings(intervals) ? "true" : "false") << std::endl;
    return 0;
}
