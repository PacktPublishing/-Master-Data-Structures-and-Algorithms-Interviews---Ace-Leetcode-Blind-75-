
function longestConsecutive(nums) {
    if (!nums || nums.length === 0) {
        return 0;
    }

    const numSet = new Set(nums);
    let longestStreak = 0;

    for (let num of numSet) {
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let currentStreak = 1;

            while (numSet.has(currentNum + 1)) {
                currentNum += 1;
                currentStreak += 1;
            }

            longestStreak = Math.max(longestStreak, currentStreak);
        }
    }

    return longestStreak;
}

// Example usage
const nums = [100, 4, 200, 1, 3, 2];
console.log("Longest consecutive sequence length:", longestConsecutive(nums));
