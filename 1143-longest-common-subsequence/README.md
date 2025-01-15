# Longest Common Subsequence (Leetcode #1143)

The Longest Common Subsequence (LCS) problem is a fundamental dynamic programming challenge that finds applications in diverse fields, from bioinformatics to text comparison tools. In this blog, we will discuss what the problem is, explore a brute-force solution, give you a hint to think about a more optimized approach, and provide a dynamic programming-based efficient solution. Let's get started!

## Understanding the Problem Statement

The goal of the Longest Common Subsequence problem is to find the longest subsequence that appears in the same order in two strings, but not necessarily consecutively. For example, given two strings `text1 = "abcde"` and `text2 = "ace"`, the longest common subsequence is `"ace"`, and its length is `3`.

The key point here is that the characters must appear in the same order, but they do not need to be consecutive. The challenge is to find the length of this common subsequence efficiently.

## Brute Force Approach

The brute-force approach to solving this problem involves generating all possible subsequences of one string and then checking which of them are also subsequences of the other string. This can be a very time-consuming task, especially if the lengths of the strings are large.

For a string of length `m`, there are `2^m` possible subsequences. Thus, generating all subsequences and checking each one against the other string is computationally infeasible for large values of `m` and `n` due to its exponential time complexity, which is `O(2^m * n)`. This makes the brute-force approach impractical for longer strings.

## Hint to Solve the Problem Efficiently

The key to optimizing the solution for LCS is recognizing overlapping sub-problems. When we try to determine the LCS, many sub-problems repeat, and a dynamic programming approach can be used to store the results of these sub-problems and avoid redundant calculations.

In other words, rather than recalculating the LCS for the same set of prefixes multiple times, we can use a table to store these results. This approach significantly reduces the computational overhead.

## Efficient Solution

Let's dive into the efficient solution provided in the code using dynamic programming. Here's how the code works:

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[m][n]
```

**Detailed Explanation**

1. **Initialization**: We create a 2D list `dp` with dimensions `(m + 1) x (n + 1)` to store the lengths of the longest common subsequence for different prefixes of `text1` and `text2`. The dimensions are `(m + 1)` and `(n + 1)` to handle empty prefixes easily by initializing the base cases to zero.
    
2. **Iterating through Characters**: We use two nested loops to iterate over each character in `text1` and `text2`. If the characters match (`text1[i - 1] == text2[j - 1]`), it means that the LCS for the current prefixes includes this character, so we add `1` to the LCS length of the previous prefixes (`dp[i - 1][j - 1] + 1`).
    
3. **Handling Non-matching Characters**: If the characters do not match, we take the maximum value from either excluding the current character of `text1` or `text2` (`max(dp[i][j - 1], dp[i - 1][j])`). This way, we ensure that the longest possible subsequence is considered.
    
4. **Result**: Finally, the value in the bottom-right cell of the table (`dp[m][n]`) represents the length of the longest common subsequence of `text1` and `text2`.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(m * n)`, where `m` is the length of `text1` and `n` is the length of `text2`. This is because we iterate over all characters in both strings, and for each pair of characters, we perform constant-time operations.
    
* **Space Complexity**: The space complexity is also `O(m * n)` due to the 2D array `dp` used to store the intermediate LCS lengths for all combinations of prefixes of `text1` and `text2`. This can be optimized to `O(n)` if we only store the previous row at any point, but the provided solution uses the full table for simplicity.
    

## Conclusion

The Longest Common Subsequence problem is a great example of how dynamic programming can be used to turn an inefficient brute-force approach into a highly efficient solution. By recognizing overlapping sub-problems and storing intermediate results, we can significantly reduce the computational cost of finding the LCS. The dynamic programming approach presented here runs in polynomial time, making it suitable for strings of reasonable length.

Hopefully, this blog helps you understand the LCS problem better and how to tackle it using dynamic programming. Try implementing the solution yourself, and see how the power of dynamic programming makes a challenging problem much more approachable!

README for [Longest Common Subsequence (Leetcode #1143)](https://blog.unwiredlearning.com/longest-common-subsequence) was compiled from the Unwired Learning Blog.