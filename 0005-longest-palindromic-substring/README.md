# Longest Palindromic Substring (Leetcode #5)

Finding the longest palindromic substring in a given string is one of the most frequently asked questions in coding interviews, especially for roles that involve algorithms and data structures. This problem not only tests your understanding of dynamic programming but also helps you master how to optimize complex solutions. In this blog, we will explore a brute force method, delve into an efficient approach using dynamic programming, and break down the time and space complexities involved. Let's dive in!

## Understanding the Problem Statement

The goal of the "Longest Palindromic Substring" problem is to find the longest substring within a given string that reads the same backward as forward. The input is a string of characters, and you need to return the longest palindromic substring. For example, if the input string is "babad", the answer could be "bab" or "aba".

## Brute Force Approach

The most intuitive way to solve this problem is the brute force method, where we generate all possible substrings and check whether each one is a palindrome. This can be done by iterating over all possible starting and ending points of the substring and then reversing each substring to verify if it matches the original.

In Python, the brute force approach might look something like this:

1. Iterate over all pairs of start and end indices.
    
2. Check if the substring is a palindrome by reversing it.
    
3. Keep track of the longest palindrome found.
    

The brute force solution will have a time complexity of O(n^3) since it takes O(n^2) to generate all substrings and O(n) to check if each substring is a palindrome.

## Hint to Solve the Problem Efficiently

A more efficient approach involves using dynamic programming to keep track of palindromes in a 2D table. The key idea here is that a substring is a palindrome if its boundary characters are equal and the substring within those boundaries is also a palindrome. By storing these intermediate results, we can avoid redundant calculations.

## Efficient Solution

Here is the provided efficient solution that leverages dynamic programming to reduce the time complexity:

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        dp = [[False] * n for _ in range(n)]
        
        # Initialize start position and max length of the palindrome
        start, max_length = 0, 1

        # Base case: single character palindromes
        for i in range(n):
            dp[i][i] = True

        # Base case: two-character palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True                
            if dp[i][i+1]:
                start, max_length = i, 2

        # General case
        for length in range(3, n+1):  
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    start, max_length = i, length

        return s[start:start+max_length]
```

**Explanation of the Code**

* **Initialization**: We first initialize a 2D list `dp` to store whether a substring is a palindrome. `dp[i][j]` is True if the substring from `i` to `j` is a palindrome.
    
* **Base Cases**: We initialize all single-character substrings as palindromes (`dp[i][i] = True`). We also handle the two-character substrings.
    
* **General Case**: We iterate through possible substring lengths, starting from 3. For each substring of a given length, we check if its boundary characters are the same and if the substring within those boundaries is also a palindrome.
    
* **Return Value**: We track the starting position and length of the longest palindromic substring found, which allows us to return the desired result.
    

## Time and Space Complexity

* **Time Complexity**: The efficient solution has a time complexity of O(n^2). This is because we fill out a 2D table of size `n x n` by iterating over all substrings of increasing length.
    
* **Space Complexity**: The space complexity is also O(n^2), as we store the results for all possible substrings in a 2D list. This helps in avoiding redundant calculations and contributes to the optimized solution.
    

## Conclusion

The "Longest Palindromic Substring" problem can initially seem challenging, especially with the brute force approach being highly inefficient. However, with the help of dynamic programming, we can significantly reduce the time complexity and solve the problem effectively. Mastering this efficient approach will not only help you tackle similar problems but also improve your overall problem-solving skills for coding interviews.

README for [Longest Palindromic Substring (Leetcode #5)](https://blog.unwiredlearning.com/longest-palindromic-substring) was compiled from the Unwired Learning Blog.