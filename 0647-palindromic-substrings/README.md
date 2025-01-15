# Palindromic Substrings (Leetcode 647)

**Palindromic Substrings** is an interesting problem that requires us to determine the number of palindromic substrings within a given string. Let's walk through the question, a brute force approach, a hint for an efficient solution, and then dive into the optimized solution, along with the associated time and space complexity.

## Understanding the Problem Statement

The problem statement is simple: Given a string `s`, count how many substrings of `s` are palindromes. A **palindrome** is a string that reads the same backward as forward, such as "aba" or "racecar". Substrings of a string are continuous parts of that string, and the question is not about distinct substrings, but the count of all palindromic substrings that exist in the given string.

For instance, given the input `s = "aaa"`, the answer would be `6`. The palindromic substrings are: "a", "a", "a", "aa", "aa", "aaa".

## Brute Force Approach

A straightforward way to solve this problem is using a **brute force** approach where you generate all possible substrings of the given string and then check if each substring is a palindrome.

Steps for the brute force approach:

1. Generate all possible substrings using nested loops.
    
2. Check if each substring is a palindrome.
    
3. Keep a count of the palindromic substrings.
    

The brute force approach is very easy to understand, but it is inefficient for longer strings. Its time complexity is **O(N^3)**, where `N` is the length of the string (`O(N^2)` for generating all substrings and another `O(N)` for checking each substring).

## Hint to Solve the Problem Efficiently

To improve efficiency, we can leverage **dynamic programming** (DP) to reduce unnecessary repeated checks. The core idea is to use a DP table to store information about whether a substring is a palindrome. This will help avoid recalculating the status of overlapping substrings, thus improving performance.

If you're unsure how to proceed, think about how you can represent subproblems (e.g., palindromic substrings) in a way that lets you build on previous results without recalculating from scratch.

## Efficient Solution

The efficient solution leverages **dynamic programming** to solve the problem in **O(N^2)** time complexity. Here's the code snippet, which follows the given approach:

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # Initialize the DP table with False.
        dp = [[False] * n for _ in range(n)]
        count = 0

        # Base case: single characters
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Base case: two consecutive characters
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1

        # DP case: substrings of length 3 to n
        for length in range(3, n+1):
            # Iterate through all starting indices for the current length.
            for i in range(n-length+1):
                # Calculate the ending index of the current substring.
                j = i+length-1

                # Check if the current substring is a palindrome.
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1

        return count
```

**Explanation of the Solution:**

* **Base Case 1:** Every single character in the string is a palindrome by itself. Thus, we initialize all `dp[i][i]` to `True`.
    
* **Base Case 2:** If two consecutive characters are equal, they form a palindromic substring of length 2. We handle this separately to make subsequent logic easier.
    
* **Dynamic Programming Logic:** For substrings longer than 2 characters, we iterate over possible lengths and check whether the current substring's boundary characters match and if the inner substring (which is shorter) is also a palindrome. If both conditions are met, the substring is palindromic.
    

## Time and Space Complexity

* **Time Complexity:** The time complexity of the dynamic programming solution is **O(N^2)**. This is due to the nested loops: the outer loop iterates over the length of substrings (from 1 to `n`), and the inner loop iterates over all possible starting points for the substring.
    
* **Space Complexity:** The space complexity is also **O(N^2)** due to the DP table (`dp`), which stores information about whether each substring is a palindrome or not.
    

The dynamic programming approach makes this problem more efficient, especially for longer strings, as it avoids recalculating palindromic conditions for overlapping substrings.

This efficient solution is a significant improvement over the brute force approach, allowing for quicker results and efficient use of computational resources.

## Conclusion

In conclusion, the problem of counting palindromic substrings can be approached in multiple ways, but leveraging dynamic programming provides a clear edge in terms of efficiency. While the brute force approach is straightforward, it becomes computationally expensive as the input size grows. The dynamic programming solution, on the other hand, reduces redundant calculations by building on previous results, making it a more scalable option. Understanding the principles of breaking down problems and optimizing with DP is crucial for tackling similar problems effectively. This approach not only enhances problem-solving skills but also equips you with techniques that are widely applicable in competitive programming and real-world scenarios.


README for [Palindromic Substrings (Leetcode 647)](https://blog.unwiredlearning.com/palindromic-substrings) was compiled from the Unwired Learning Blog.