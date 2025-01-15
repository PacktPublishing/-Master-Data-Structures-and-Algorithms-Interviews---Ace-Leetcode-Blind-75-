
#include <iostream>
#include <vector>
#include <algorithm>

int eraseOverlapIntervals(std::vector<std::pair<int, int>> intervals) {
    std::sort(intervals.begin(), intervals.end());

    int prev_end = intervals[0].second;
    int count = 0;

    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i].first < prev_end) {
            count++;
            prev_end = std::min(prev_end, intervals[i].second);
        } else {
            prev_end = intervals[i].second;
        }
    }

    return count;
}

int main() {
    std::vector<std::pair<int, int>> intervals = {{1, 2}, {2, 3}, {3, 4}, {1, 3}};
    std::cout << eraseOverlapIntervals(intervals) << std::endl;
    return 0;
}
