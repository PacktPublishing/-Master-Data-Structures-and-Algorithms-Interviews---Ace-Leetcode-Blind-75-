
public class MissingNumber {
    public static int missingNumber(int[] nums) {
        int xor = 0;
        int n = nums.length;

        // XOR all indices and all elements in nums
        for (int i = 0; i < n; i++) {
            xor = xor ^ i ^ nums[i];
        }

        // Finally XOR with n (since the range is from 0 to n)
        xor = xor ^ n;

        return xor;
    }

    public static void main(String[] args) {
        int[] nums = {3, 0, 1};
        System.out.println(missingNumber(nums));  // Output: 2
    }
}
