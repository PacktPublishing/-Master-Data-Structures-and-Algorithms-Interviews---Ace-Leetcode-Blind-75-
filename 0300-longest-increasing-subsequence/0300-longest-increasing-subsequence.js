
function lengthOfLIS(nums) {
    if (nums.length === 0) {
        return 0;
    }

    let dp = new Array(nums.length).fill(1);
    let max_length = 1;

    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        max_length = Math.max(max_length, dp[i]);
    }

    return max_length;
}
