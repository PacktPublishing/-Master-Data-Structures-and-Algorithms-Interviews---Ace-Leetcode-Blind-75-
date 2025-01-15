# Number of 1 Bits (Leetcode #191)

Finding the number of 1 bits in a binary representation of a number is a common problem in computer science. In this blog, we'll take you through the solution to the problem "Number of 1 Bits," also known as calculating the Hamming Weight. We'll discuss a brute-force approach, provide hints to tackle the problem efficiently, and ultimately dive into the provided optimized code. Let's begin!

## Understanding the Problem Statement

The problem is simple: You are given an unsigned integer, and you need to determine how many '1' bits are present in its binary representation. This is also called finding the Hamming Weight of the number.

For example:

* Input: `n = 11` (binary representation: `00000000000000000000000000001011`)
    
* Output: `3`
    

The output is `3` because the binary representation of `11` contains three '1' bits.

## Brute Force Approach

A brute-force way to solve this problem involves converting the integer to its binary string representation and then counting the '1' characters in that string.

Here's a simple implementation of the brute-force solution:

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```

In this approach, we convert `n` to a binary string using `bin(n)` and then simply count the number of '1' bits. While this method is easy to understand, it is not the most efficient in terms of bitwise operations.

## Hint to Solve the Problem Efficiently

To solve the problem more efficiently, consider using bitwise operations. Remember that we can use bit manipulation to check each bit of the number directly, without converting it to a string.

The provided code follows an efficient approach using bitwise operations to minimize unnecessary computations and keep the solution within constant time.

## Efficient Solution

The code provided takes a bitwise approach by iterating through each bit of a 32-bit integer. Here is the provided solution:

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # Assuming a 32-bit integer
        for _ in range(32):  
            # Check the LSB
            count = count + (n & 1)

            # Right shift the bits of n
            n = n >> 1                

        return count
```

**Explanation**:

1. **Initialize** `count`: We start by initializing a variable `count` to `0`. This will be used to store the number of '1' bits.
    
2. **Iterate through 32 Bits**: Since we are assuming a 32-bit integer, we loop 32 times.
    
3. **Check the Least Significant Bit (LSB)**: In each iteration, we use the bitwise AND operation (`n & 1`) to check if the least significant bit is `1`. If it is, we increment `count`.
    
4. **Right Shift** `n`: After checking the LSB, we right-shift `n` by 1 (`n >> 1`) to process the next bit in the following iteration.
    
5. **Return the** `count`: After iterating through all 32 bits, we return the value of `count`.
    

This solution is both space-efficient and computationally efficient, as it directly manipulates the bits of the integer without needing additional storage or conversions.

## Time and Space Complexity Analysis

* **Time Complexity**: `O(1)` - The loop runs for a constant 32 iterations, regardless of the input value.
    
* **Space Complexity**: `O(1)` - No extra space is used apart from the variable `count`.
    

Thus, this solution operates in constant time and constant space, making it very efficient for this problem.

## Conclusion

The "Number of 1 Bits" problem provides a great opportunity to practice bitwise operations, which are a powerful tool in optimizing solutions for binary representation problems. While the brute-force method using string operations is easy to understand, the bitwise approach used in the provided solution is significantly more efficient and teaches us about bit manipulation techniques.

We hope this guide has helped you understand both a simple and an efficient way to solve this problem. Happy coding!

README for [Number of 1 Bits (Leetcode #191)](https://blog.unwiredlearning.com/number-of-1-bits) was compiled from the Unwired Learning Blog.