
#include <iostream>
#include <vector>

using namespace std;

int missingNumber(vector<int>& nums) {
    int xor_result = 0;
    int n = nums.size();

    // XOR all indices and all elements in nums
    for (int i = 0; i < n; i++) {
        xor_result = xor_result ^ i ^ nums[i];
    }

    // Finally XOR with n (since the range is from 0 to n)
    xor_result = xor_result ^ n;

    return xor_result;
}

int main() {
    vector<int> nums = {3, 0, 1};
    cout << missingNumber(nums) << endl;  // Output: 2

    return 0;
}
