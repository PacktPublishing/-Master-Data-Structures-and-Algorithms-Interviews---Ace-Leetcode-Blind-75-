# Longest Repeating Character Replacement (Leetcode #424)

Leetcode's problem "Longest Repeating Character Replacement" (Problem 424) is an intriguing challenge that tests your understanding of string manipulation and sliding window techniques. The problem statement is quite relatable for those dealing with character strings, and it also serves as a great exercise for coding interviews. Let's break down the question, explore different approaches, and finally walk through an efficient solution.

## Understanding the Problem Statement

You are given a string `s` and an integer `k`. You can replace up to `k` characters in the string, and your goal is to find the length of the longest substring containing the same letter you can get after making those replacements. The problem boils down to determining the longest contiguous substring where you can replace no more than `k` characters to make all the characters identical.

For instance, if you have the string `s = "AABABBA"` and `k = 1`, the output should be `4`, because you can replace one character (`B` at index 4) to make the substring "AABA".

## Brute Force Approach

A common brute-force approach for solving this problem is to check every possible substring, determining if you can make it uniform with no more than `k` changes. Here's a basic outline:

1. Iterate through all possible substrings.
    
2. For each substring, count how many changes are needed to make all characters the same.
    
3. Keep track of the maximum length that meets the `k`\-replacement requirement.
    

While this approach works, it is extremely inefficient, with a time complexity of `O(n^2)` or worse, given that each substring must be evaluated, and then modified accordingly. This quickly becomes impractical for larger strings.

## Hint to Solve the Problem Efficiently

The key to solving this problem efficiently is to use the **sliding window technique**. Instead of evaluating every possible substring, you can dynamically expand and contract a window over the string, keeping track of important metrics as you go along. This allows you to find the solution in linear time.

In the sliding window, you need to keep track of the **most frequent character** within the window. The number of other characters can be replaced to maximize the window length. If the number of replacements exceeds `k`, the window should be contracted from the left.

## Efficient Solution

Below is an efficient Python solution that leverages the sliding window technique. The core idea is to maintain a window of characters, adjusting its boundaries to maximize the number of identical characters after no more than `k` replacements.

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len = 0
        left = 0
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
```

**Explanation**:

1. **Initialize Variables**: Start by defining a dictionary `count` to store character frequencies, `max_len` for tracking the maximum length found, and pointers `left` and `right` to define the sliding window boundaries.
    
2. **Expand Window**: Use `right` to expand the window and add characters to the frequency dictionary. Also, update `max_freq` to maintain the count of the most frequent character in the window.
    
3. **Contract Window**: If the current window size minus the frequency of the most frequent character exceeds `k`, it means we need to reduce the size of the window from the left to meet the constraint.
    
4. **Update Maximum Length**: Finally, update `max_len` to track the longest valid window found.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(n)`, where `n` is the length of the string. The sliding window ensures that each character is visited at most twice (once when expanding and once when contracting), resulting in a linear time complexity.
    
* **Space Complexity**: The space complexity is `O(1)` or `O(26)` to be precise, because the `count` dictionary can store up to 26 characters at most (considering only uppercase English letters), which is effectively a constant space requirement.
    

## Conclusion

The "Longest Repeating Character Replacement" problem is a great example of how the sliding window technique can dramatically reduce the complexity of a problem involving contiguous subarrays or substrings. The brute force solution, while conceptually straightforward, is inefficient for larger strings, whereas the sliding window approach yields a much more practical and performant solution.

If you're looking to improve your skills in tackling similar problems, mastering sliding window techniques like this is invaluable, especially in coding interviews.


README for [Longest Repeating Character Replacement (Leetcode #424))](https://blog.unwiredlearning.com/longest-repeating-character-replacement) was compiled from the Unwired Learning Blog.