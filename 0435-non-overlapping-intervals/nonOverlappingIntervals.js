
function eraseOverlapIntervals(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);

    let prev_end = intervals[0][1];
    let count = 0;

    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < prev_end) {
            count++;
            prev_end = Math.min(prev_end, intervals[i][1]);
        } else {
            prev_end = intervals[i][1];
        }
    }

    return count;
}

// Example usage:
let intervals = [[1, 2], [2, 3], [3, 4], [1, 3]];
console.log(eraseOverlapIntervals(intervals));
