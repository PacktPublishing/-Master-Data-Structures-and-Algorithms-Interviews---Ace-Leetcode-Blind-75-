
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    vector<vector<int>> left, right;
    int start = newInterval[0], end = newInterval[1];

    for (auto& i : intervals) {
        if (i[1] < start) {
            left.push_back(i);
        } else if (i[0] > end) {
            right.push_back(i);
        } else {
            start = min(start, i[0]);
            end = max(end, i[1]);
        }
    }

    left.push_back({start, end});
    left.insert(left.end(), right.begin(), right.end());

    return left;
}

int main() {
    vector<vector<int>> intervals = {{1, 3}, {6, 9}};
    vector<int> newInterval = {2, 5};
    vector<vector<int>> result = insert(intervals, newInterval);

    for (auto& interval : result) {
        cout << "[" << interval[0] << ", " << interval[1] << "]" << endl;
    }

    return 0;
}
