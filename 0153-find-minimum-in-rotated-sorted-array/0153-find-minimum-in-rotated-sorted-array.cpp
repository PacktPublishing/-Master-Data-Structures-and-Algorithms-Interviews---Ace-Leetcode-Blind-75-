#include <vector>

class Solution {
public:
    int findMin(std::vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

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
};