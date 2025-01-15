function threeSum(nums) {
    nums.sort((a, b) => a - b);
    const result = [];
    
    for (let i = 0; i < nums.length - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue; // Skip duplicates for the first number
        }
        
        let left = i + 1;
        let right = nums.length - 1;
        
        while (left < right) {
            const total = nums[i] + nums[left] + nums[right];
            if (total === 0) {
                result.push([nums[i], nums[left], nums[right]]);
                
                while (left < right && nums[left] === nums[left + 1]) {
                    left++; // Skip duplicates for the second number
                }
                while (left < right && nums[right] === nums[right - 1]) {
                    right--; // Skip duplicates for the third number
                }
                
                left++;
                right--;
            } else if (total < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    return result;
}