# Two Sum (Leetcode #1)

Leetcode's 'Two Sum' question is a classic problem that tests your understanding of array manipulation, hash maps, and time complexity optimization. Let's break it down step-by-step:

### **Understanding the Question**

In the 'Two Sum' problem, you are given an array of integers, `nums`, and an integer `target`. Your task is to find two distinct indices in the array such that the sum of the numbers at those indices equals the `target`.

You need to return the indices of the two numbers, and the solution should satisfy the following conditions:

* There must be exactly **one solution** (no repeated pairs).
    
* You **cannot use the same element twice**.
    

For example, given `nums = [2, 7, 11, 15]` and `target = 9`, the solution would return `[0, 1]` because `2 + 7 = 9`.

### **Brute Force Approach**

The simplest approach is to use two nested loops to check all possible pairs of numbers in the array. Here's the pseudocode for the brute force approach:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

* **Explanation:**
    
    * The outer loop picks an element, and the inner loop checks every subsequent element to find a pair that sums to the target.
        
* **Time Complexity:**  
    This approach takes `O(n^2)`, where nnn is the length of the array. This is because for each element, you are iterating over the remaining elements to find a matching pair.
    
* **Space Complexity:**  
    The space complexity is `O(1)`, as no extra data structures are used except for a constant number of variables.
    

### **Efficient Solution**

The brute force solution is inefficient for large datasets. To improve, we can use a **hashmap** (or dictionary) to store numbers and their indices while iterating through the array. The provided efficient solution achieves this in a single pass.

Here’s the Python solution code provided:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in hashmap:
                return [hashmap[complement], i]
            
            hashmap[nums[i]] = i
```

* **Explanation:**
    
    * **hashmap = {}:** We use a hashmap (or dictionary) to store the elements as keys and their indices as values.
        
    * **complement = target - nums\[i\]:** For each element `nums[i]`, we compute its complement, which is the value we need to find in the hashmap to reach the target sum.
        
    * **if complement in hashmap:** If the complement exists in the hashmap, that means we have already encountered the number that, when added to `nums[i]`, equals the target.
        
    * **return \[hashmap\[complement\], i\]:** If the complement is found, return the indices of the two numbers.
        
    * **hashmap\[nums\[i\]\] = i:** If the complement is not found, store the current number and its index in the hashmap for future reference.
        

### **Time and Space Complexity**

* **Time Complexity:**  
    The time complexity of this solution is `O(n)`, where `n` is the length of the input array. This is because we only traverse the array once, and both the lookup and insertion operations in a hashmap are `O(1)` on average.
    
* **Space Complexity:**  
    The space complexity is `O(n)`, where `n` is the number of elements in the array. This is because we are storing up to `n` elements in the hashmap.
    

### Conclusion

The optimized solution using a hashmap reduces the time complexity from `O(n^2)` in the brute force approach to `O(n)`. It’s efficient and works well even with large datasets, making it an ideal solution for this problem.

By understanding and implementing this technique, you can effectively tackle similar problems that involve pair sums or finding elements in arrays based on certain conditions.


README for [Two Sum (Leetcode #1)](https://blog.unwiredlearning.com/two-sum) was compiled from the Unwired Learning Blog.