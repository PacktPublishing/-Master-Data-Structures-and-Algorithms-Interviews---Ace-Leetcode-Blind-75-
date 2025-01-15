
function merge(intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    let merged = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        let lastInterval = merged[merged.length - 1];
        if (intervals[i][0] <= lastInterval[1]) {
            lastInterval[1] = Math.max(lastInterval[1], intervals[i][1]);
        } else {
            merged.push(intervals[i]);
        }
    }

    return merged;
}

// Example usage:
let intervals = [[1, 3], [2, 6], [8, 10], [15, 18]];
console.log(merge(intervals));
