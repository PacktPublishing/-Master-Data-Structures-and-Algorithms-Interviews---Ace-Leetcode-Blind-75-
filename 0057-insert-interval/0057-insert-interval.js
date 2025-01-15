
function insert(intervals, newInterval) {
    let left = [], right = [];
    let [start, end] = newInterval;

    for (let i of intervals) {
        if (i[1] < start) {
            left.push(i);
        } else if (i[0] > end) {
            right.push(i);
        } else {
            start = Math.min(start, i[0]);
            end = Math.max(end, i[1]);
        }
    }

    return [...left, [start, end], ...right];
}

// Example usage:
let intervals = [[1, 3], [6, 9]];
let newInterval = [2, 5];
console.log(insert(intervals, newInterval));
