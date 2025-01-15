# Decode Ways (Leetcode #91)

Have you ever wondered how a sequence of numbers could be translated into meaningful text, similar to decoding a secret message? The **"Decode Ways"** problem is a classic challenge that invites you to determine how many ways a given sequence of digits can be decoded into letters. In this blog, we'll explore how to solve this problem using different approaches, starting with a brute force method and eventually moving towards a more efficient solution using dynamic programming.

## Understanding the Problem Statement

The **"Decode Ways"** problem involves decoding a string of digits, where each character represents a digit between '1' and '9'. These digits map to letters in the alphabet as follows:

* '1' maps to 'A'
    
* '2' maps to 'B'
    
* ...
    
* '26' maps to 'Z'
    

Given a string `s` consisting of only digits, the objective is to determine the number of ways it can be decoded into letters. The rules are:

* Each digit can be decoded on its own (if it is between '1' and '9').
    
* A pair of two consecutive digits can also be decoded if it represents a valid character (i.e., a number between '10' and '26').
    
* Sequences starting with '0' are invalid and cannot be decoded.
    

For example:

* Input: "12" Output: 2 Explanation: "12" can be decoded as "AB" (1, 2) or "L" (12).
    
* Input: "226" Output: 3 Explanation: "226" can be decoded as "BZ" (2, 26), "VF" (22, 6), or "BBF" (2, 2, 6).
    

## Brute Force Approach

A straightforward way to solve this problem is through a brute force approach, which involves recursively considering every possible way to split the given string:

1. Start with the first character and check if it forms a valid letter ('1' to '9'). If it does, recursively proceed with the rest of the string.
    
2. Similarly, check if the first two characters together form a valid letter ('10' to '26'). If so, recursively decode the remainder of the string.
    

This method explores all possible decoding paths. While this approach is simple, it is highly inefficient due to the repeated recalculation of overlapping subproblems, especially for long strings.

**Drawbacks of the Brute Force Approach:**

* **Time Complexity:** The time complexity is exponential, as it involves exploring every possible combination of valid splits.
    
* **Space Complexity:** The recursive calls lead to a significant usage of the call stack, increasing space complexity.
    

## Hint to Solve the Problem Efficiently

The dynamic programming approach aims to solve this problem by storing intermediate results to avoid recalculating the same subproblems. By utilizing an array (`dp`) to keep track of the number of ways to decode substrings of various lengths, we can build on previous results to derive the final answer in a more efficient manner.

## Efficient Solution

The efficient solution for the **"Decode Ways"** problem uses dynamic programming, as illustrated in the provided code below:

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        # Base cases
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            # Single digit decode
            if 1 <= int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]

            # Two digit decode
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[n]
```

**Explanation:**

* **Base Cases:**
    
    * `dp[0]` is set to 1, representing an empty string that can be decoded in one way.
        
    * `dp[1]` is set to 1 because a single valid digit can be decoded in one way, as long as it is not '0'.
        
* **Iterative Calculation:**
    
    * We iterate over the string starting from index 2.
        
    * For each character, we check if the single-digit value (`s[i-1:i]`) is valid (between '1' and '9'). If it is, we add the number of ways to decode up to the previous character (`dp[i-1]`).
        
    * We also check if the two-digit value (`s[i-2:i]`) is valid (between '10' and '26'). If so, we add the number of ways to decode up to the character before the last two (`dp[i-2]`).
        

This approach avoids redundant calculations by storing intermediate results, making it far more efficient than the brute force approach.

## Time and Space Complexity

* **Time Complexity:** The time complexity of the dynamic programming solution is **O(n)**, where `n` is the length of the input string. This is because we iterate over the entire string once, and each operation takes constant time.
    
* **Space Complexity:** The space complexity is **O(n)** due to the use of the `dp` array of size `n + 1`. However, this could be further optimized to **O(1)** by using just two variables to keep track of the last two results instead of maintaining an entire array.
    

## Conclusion

The **"Decode Ways"** problem is a great exercise for understanding how to apply dynamic programming to problems involving overlapping subproblems and multiple recursive calls. By storing intermediate results and building upon them, we can achieve a significant reduction in time complexity compared to the brute force approach. We hope this blog has given you a clear understanding of both the brute force and dynamic programming approaches to solving this problem, and provided you with insights into optimizing your solutions for similar challenges.

README for [Decode Ways  (Leetcode #91)](https://blog.unwiredlearning.com/decode-ways) was compiled from the Unwired Learning Blog.