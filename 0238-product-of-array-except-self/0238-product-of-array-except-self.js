
function productExceptSelf(nums) {
    const n = nums.length;

    // Array to store all left multiplication
    const left = Array(n).fill(1);
    for (let i = 1; i < n; i++) {
        left[i] = left[i - 1] * nums[i - 1];
    }

    // Array to store all right multiplication
    const right = Array(n).fill(1);
    for (let i = n - 2; i >= 0; i--) {
        right[i] = right[i + 1] * nums[i + 1];
    }

    // Calculate the result array by multiplying left and right products
    const result = Array(n);
    for (let i = 0; i < n; i++) {
        result[i] = left[i] * right[i];
    }

    return result;
}
