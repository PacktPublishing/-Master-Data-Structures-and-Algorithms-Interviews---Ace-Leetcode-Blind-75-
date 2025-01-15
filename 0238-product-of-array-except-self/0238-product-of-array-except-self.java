
import java.util.*;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        // Array to store all left multiplication
        int[] left = new int[n];
        Arrays.fill(left, 1);
        for (int i = 1; i < n; i++) {
            left[i] = left[i - 1] * nums[i - 1];
        }

        // Array to store all right multiplication
        int[] right = new int[n];
        Arrays.fill(right, 1);
        for (int i = n - 2; i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }

        // Calculate the result array by multiplying left and right products
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = left[i] * right[i];
        }

        return result;
    }
}
