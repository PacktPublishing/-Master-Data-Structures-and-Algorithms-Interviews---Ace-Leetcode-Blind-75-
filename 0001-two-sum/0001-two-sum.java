import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (hashmap.containsKey(complement)) {
                return new int[] {hashmap.get(complement), i};
            }

            hashmap.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

// Question: https://leetcode.com/problems/two-sum
// Blog: https://blog.unwiredlearning.com/two-sum