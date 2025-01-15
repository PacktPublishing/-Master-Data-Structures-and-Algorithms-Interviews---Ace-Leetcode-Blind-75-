# Counting Bits (Leetcode #338)

Leetcode's "Counting Bits" problem is a fascinating challenge that tests our understanding of binary numbers and efficient problem-solving. In this blog, we will walk through the problem, explore a common brute-force approach, and then provide you with a hint to solve it efficiently. We'll conclude by explaining an optimal solution step-by-step and analyzing its time and space complexity.

## Understanding the Problem Statement

In the "Counting Bits" problem (Leetcode 338), we are given a non-negative integer `n`, and the task is to return an array `ans` of length `n + 1`, where `ans[i]` is the number of `1` bits in the binary representation of the number `i`. Essentially, you need to count the number of `1`s (also known as set bits) for each number from `0` to `n` and return all those counts in an array.

For example:

* **Input**: `n = 5`
    
* **Output**: `[0, 1, 1, 2, 1, 2]`
    
* **Explanation**: The binary representations are `0 -> 0`, `1 -> 1`, `2 -> 10`, `3 -> 11`, `4 -> 100`, `5 -> 101`. Hence, the counts of set bits are `0, 1, 1, 2, 1, 2` respectively.
    

## Brute Force Approach

A straightforward way to solve this problem is to iterate through each number from `0` to `n` and count the number of `1`s in its binary representation. This can be done by repeatedly shifting the bits of each number and counting how many bits are set. Here is a brief explanation of the brute-force approach:

1. Create an empty list to store the counts.
    
2. Loop through each number from `0` to `n`.
    
3. For each number, use bitwise operations to count the `1` bits.
    
4. Append the count to the result list.
    

However, the brute force approach is not efficient for larger values of `n`, as it requires a significant amount of computation for each number, leading to a higher time complexity.

## Hint to Solve the Problem Efficiently

To solve the problem efficiently, we can leverage the properties of binary representation. Notice that if `i` is even, its set bits are equal to the set bits of `i // 2`. If `i` is odd, its set bits are one more than the set bits of `i // 2`. This observation allows us to compute the number of set bits in constant time for each number based on the previously computed values.

## Efficient Solution

The provided code takes advantage of the above observation to efficiently solve the problem. Here is the code and an explanation of how it works:

```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize a list to store the result
        result = [0] * (n + 1)
        
        # If n is 0, simply return the result list (which is [0])
        if n == 0:
            return result
        
        # The number of 1's in the binary representation of 1 is 1
        result[1] = 1
        
        # Loop through numbers from 2 to n
        for i in range(2, n + 1):
            if i % 2 == 0:
                result[i] = result[i // 2]
            else:
                result[i] = result[i // 2] + 1
        
        return result
```

**Explanation**:

1. **Initialization**: We initialize a list `result` of size `n + 1` with all values set to `0`.
    
2. **Base Cases**: If `n` is `0`, we directly return `[0]`. We also set `result[1] = 1` since `1` has one set bit.
    
3. **Loop through** `2` **to** `n`: For each number `i`, we determine the number of set bits based on whether `i` is even or odd:
    
    * If `i` is even, `result[i] = result[i // 2]`.
        
    * If `i` is odd, `result[i] = result[i // 2] + 1`.
        

This approach is efficient because it calculates each value in constant time using previously computed values, resulting in an optimal solution.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(n)` since we iterate through all numbers from `0` to `n`, and each computation takes constant time.
    
* **Space Complexity**: The space complexity is `O(n)` due to the additional space needed to store the result array of size `n + 1`.
    

## Conclusion

The "Counting Bits" problem is a great way to understand the efficiency of dynamic programming and the power of using previously computed results to optimize the solution. By recognizing patterns in the binary representation of numbers, we are able to achieve an efficient `O(n)` solution instead of the costly brute-force approach. This problem also emphasizes the importance of recognizing subproblems and utilizing existing results for more efficient computation.

README for [Counting Bits (Leetcode #338)](https://blog.unwiredlearning.com/counting-bits) was compiled from the Unwired Learning Blog.