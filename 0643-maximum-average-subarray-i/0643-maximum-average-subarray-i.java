import java.util.*;

class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // Sum for starting window
        int currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += nums[i];
        }

        int maxSum = currentSum;

        // Start sliding window
        int startIndex = 0;
        int endIndex = k;

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
        return (double) maxSum / k;
    }
}
