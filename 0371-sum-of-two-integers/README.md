# Sum of Two Integers (Leetcode #371)

In this blog, we'll dive into an intriguing problem from LeetCode: **Sum of Two Integers (Problem 371)**. We'll explore a basic brute force approach, understand a hint to approach it more efficiently, and finally provide an optimal solution. This problem challenges us to sum two integers without using the addition or subtraction operators, making it an interesting exercise in bitwise operations.

## Understanding the Problem Statement

The problem asks us to find the sum of two integers **a** and **b** without using the **+** or **\-** operators. At first glance, it might sound unusual because we often rely on these operators for addition and subtraction. However, we can solve this using bitwise operations like **AND**, **XOR**, and **left shift**, which are fundamental to computer arithmetic.

## Brute Force Approach

A common brute force approach to solving this problem could be to repeatedly increment one of the numbers until we reach the sum. Essentially, we could use a loop to add **1** to **a** for **b** number of times. This approach would look like the following:

* If **b** is positive, increment **a** by **1** for each step until **b** is zero.
    
* If **b** is negative, decrement **a** similarly.
    

However, this approach would be highly inefficient for large values of **b**, as it requires **O(b)** iterations, which is not feasible for large numbers.

## Hint to Solve the Problem Efficiently

The key to solving this problem lies in understanding how addition can be represented using bitwise operations. Recall that:

* **XOR (a ^ b)** adds bits without considering any carry.
    
* **AND (a & b)** followed by a left shift (**&lt;&lt; 1**) helps us determine the carry bits.
    

By combining these two operations iteratively, we can achieve the desired sum without using the **+** operator.

## Efficient Solution

Here is the efficient solution provided in the attached code:

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit integer max value
        MAX = 0x7FFFFFFF
        
        # Mask to get 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            # Calculate the carry bits
            carry = (a & b) & mask
            
            # XOR the bits for sum without carry
            a = (a ^ b) & mask
            
            # Shift the carry to add in the next higher bit position
            b = (carry << 1) & mask
        
        # If a is negative, return a's complement in Python's 32-bit format
        return a if a <= MAX else ~(a ^ mask)
```

Let's break down how this solution works:

1. **Initialize Constants**: We define **MAX** as the maximum value for a 32-bit integer and use **mask** to ensure we only deal with 32 bits.
    
2. **Loop Until No Carry**: The loop continues as long as there is a carry. The carry is calculated using **a & b**, which gives the positions where both **a** and **b** have **1s**.
    
3. **XOR for Sum**: We use **a ^ b** to add **a** and **b** without the carry.
    
4. **Shift Carry**: The carry is shifted left by one position so that it can be added to the next higher bit.
    
5. **Handle Negative Numbers**: If **a** exceeds the maximum positive value for a 32-bit integer, it means **a** is negative, and we return its complement.
    

This approach efficiently computes the sum in **O(1)** time complexity, as it only involves a fixed number of bitwise operations.

## Time and Space Complexity

* **Time Complexity**: The time complexity is **O(1)** because the number of operations is constant and does not depend on the size of **a** or **b**.
    
* **Space Complexity**: The space complexity is **O(1)** as we are only using a constant amount of extra space.
    

## Conclusion

The **Sum of Two Integers** problem is a great example of how we can leverage bitwise operations to perform arithmetic tasks without relying on traditional operators. By understanding the mechanics of **XOR** and **AND** operations, we can solve this problem in an efficient manner. If you're preparing for technical interviews, mastering such bitwise tricks can give you an edge, especially when faced with low-level manipulation challenges.

README for [Sum of Two Integers (Leetcode #371)](https://blog.unwiredlearning.com/sum-of-two-integers) was compiled from the Unwired Learning Blog.