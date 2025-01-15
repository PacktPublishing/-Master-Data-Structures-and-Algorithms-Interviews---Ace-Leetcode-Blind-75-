# Is Subsequence (Leetcode #392)

In this blog, we will explore the LeetCode problem "Is Subsequence." We'll break down the problem statement, look at a common brute force approach, provide a hint for an efficient solution, and ultimately discuss the optimal way to solve it. By the end of this blog, you'll have a clear understanding of how to tackle this problem effectively.

## Understanding the Problem Statement

The problem "Is Subsequence" asks you to determine whether a given string `s` is a subsequence of another string `t`. A subsequence is a sequence derived from another string by deleting some (or none) of the characters without changing the order of the remaining characters.

For example:

* `s = "abc"`, `t = "ahbgdc"` — In this case, `s` is a subsequence of `t`.
    
* `s = "axc"`, `t = "ahbgdc"` — Here, `s` is **not** a subsequence of `t` because the characters do not match in the required order.
    

The task is to return `true` if `s` is a subsequence of `t`, otherwise return `false`.

## Brute Force Approach

A naive approach to solve this problem could be generating all possible subsequences of the string `t` and then checking if `s` matches any of those subsequences. However, generating all subsequences involves exponential complexity, making it highly impractical for larger strings.

The brute force approach has a time complexity of **O(2^n)**, where `n` is the length of `t`. This complexity arises because we need to consider every possible combination of characters from `t`.

## Hint to Solve the Problem Efficiently

Instead of generating subsequences, we can iterate through `t` while attempting to "match" the characters of `s` in sequence. We use two pointers: one for `s` and one for `t`. By carefully moving these pointers, we can determine whether `s` can be found within `t` while maintaining the order of characters.

The key idea is:

* Use a pointer to track your position in both strings and move through `t` to see if all characters in `s` are matched.
    

## Efficient Solution

Here is an efficient solution that utilizes two pointers to iterate over the strings `s` and `t`:

```python
class Solution:
    def isSubsequence(self, str1: str, str2: str) -> bool:
        # Initialize pointers for both strings
        itr1, itr2 = 0, 0
        
        # Iterate while both pointers are within their respective strings
        while itr1 < len(str1) and itr2 < len(str2):
            # Compare characters; if they match, move both pointers
            if str1[itr1] == str2[itr2]:
                itr1 += 1
                itr2 += 1
            else:
                itr2 += 1  # Move pointer for str2 only

        # If 'itr1' has reached the length of 'str1', it means all characters are matched
        return itr1 == len(str1)
```

**How the Solution Works**

* **Pointers Initialization**: We start with two pointers: `itr1` for `str1` (i.e., `s`) and `itr2` for `str2` (i.e., `t`). Both pointers are initially set to 0.
    
* **Iteration**: The loop continues until one of the pointers reaches the end of its respective string. If the characters pointed to by `itr1` and `itr2` match, we increment both pointers. Otherwise, we move the pointer for `t` (`itr2`) only.
    
* **Final Check**: After the loop ends, if `itr1` has reached the end of `str1`, it means we successfully matched all characters of `s` within `t`.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(n)**, where `n` is the length of `t`. We iterate through `t` while potentially moving the pointer for `s` whenever a match is found. Since both pointers traverse their strings linearly, the time complexity is linear relative to the length of `t`.
    
* **Space Complexity**: The space complexity of this solution is **O(1)**. The solution only uses a constant amount of extra space for the two pointers, and no additional data structures are needed.
    

## Conclusion

The efficient approach for solving the "Is Subsequence" problem avoids the need for generating all possible subsequences. Instead, by leveraging two pointers, we can traverse the strings effectively in linear time. This makes the solution optimal and well-suited for larger inputs.

If you have further questions or would like more examples, feel free to comment below or check out more tutorials on efficient string manipulation!


README for [Is Subsequence (Leetcode #392)](https://blog.unwiredlearning.com/is-subsequence) was compiled from the Unwired Learning Blog.