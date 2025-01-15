class Solution {
    findMin(nums) {
        let left = 0;
        let right = nums.length - 1;

        while (left < right) {
            let mid = Math.floor(left + (right - left) / 2);

            // If the middle element is greater than the rightmost element,
            // it indicates that the smallest element is in the right half.
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // At the end of the loop, left will be pointing at the smallest element.
        return nums[left];
    }
}