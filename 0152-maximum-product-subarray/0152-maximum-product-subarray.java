
public class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int leftProduct = 1, rightProduct = 1;
        int result = nums[0];

        for (int i = 0; i < n; i++) {
            // If any of left or right product becomes 0, update it to 1
            if (leftProduct == 0) {
                leftProduct = 1;
            }
            if (rightProduct == 0) {
                rightProduct = 1;
            }

            // Prefix product
            leftProduct *= nums[i];

            // Suffix product
            rightProduct *= nums[n - 1 - i];

            // Update the result with the maximum value found
            result = Math.max(result, Math.max(leftProduct, rightProduct));
        }

        return result;
    }
}
