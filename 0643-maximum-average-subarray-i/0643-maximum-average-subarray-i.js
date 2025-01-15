/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    // Sum for starting window
    let currentSum = 0;
    for (let i = 0; i < k; i++) {
        currentSum += nums[i];
    }

    let maxSum = currentSum;

    // Start sliding window
    let startIndex = 0;
    let endIndex = k;

    while (endIndex < nums.length) {
        // Remove previous element
        currentSum -= nums[startIndex];
        startIndex++;

        // Add next element
        currentSum += nums[endIndex];
        endIndex++;

        // Update max sum
        maxSum = Math.max(maxSum, currentSum);
    }

    // Return the average
    return maxSum / k;
};
