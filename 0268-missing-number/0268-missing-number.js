
function missingNumber(nums) {
    let xor = 0;
    let n = nums.length;

    // XOR all indices and all elements in nums
    for (let i = 0; i < n; i++) {
        xor = xor ^ i ^ nums[i];
    }

    // Finally XOR with n (since the range is from 0 to n)
    xor = xor ^ n;

    return xor;
}

// Example usage:
let nums = [3, 0, 1];
console.log(missingNumber(nums));  // Output: 2
