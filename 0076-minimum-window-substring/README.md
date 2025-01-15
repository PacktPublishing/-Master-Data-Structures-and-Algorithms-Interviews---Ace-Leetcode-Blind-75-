# Minimum Window Substring (Leetcode #76)

The "Minimum Window Substring" problem is a classic challenge often featured in coding interviews, especially on platforms like LeetCode. It requires a blend of logical thinking and an understanding of efficient algorithms, making it a great test of problem-solving skills. The objective is to find the smallest substring of a given string that contains all the characters of another string. This guide will walk you through understanding the problem, exploring a brute force solution, and ultimately implementing an optimized approach using the sliding window technique.

## Understanding the Problem Statement

The "Minimum Window Substring" problem from LeetCode, labeled as problem number 76, is one that challenges your problem-solving skills and knowledge of efficient sliding window techniques. Given two strings `s` (the source string) and `t` (the target string), the task is to find the minimum window in `s` which will contain all the characters in `t` (including duplicates, if any) in any order. If no such window exists, you return an empty string.

In simpler terms, you need to find the smallest substring of `s` that includes every character from `t`. For instance, given `s = "ADOBECODEBANC"` and `t = "ABC"`, the minimum window substring is `"BANC"`. The goal is to determine the optimal window in which all characters of `t` are found.

## Brute Force Approach

The brute force solution involves checking all possible substrings of `s` to find the smallest one that contains all characters of `t`. Essentially, we iterate through every substring of `s`, and for each substring, we verify if all characters from `t` are present.

However, this approach is very inefficient, with a time complexity of `O(N^3)` for strings of length `N`, because we are generating every possible substring, checking for the presence of characters, and doing this for each character in `s`. It is not feasible for large inputs and quickly becomes impractical.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, you need to utilize the "Sliding Window" technique, which allows you to keep track of a current window that expands and contracts as needed. Here are a few hints to help you:

1. Use two pointers, `left` and `right`, to represent the current window in `s`. Start by expanding the window by moving `right` to include characters until all characters of `t` are present.
    
2. Once all characters are included, start contracting the window from the `left` to minimize the size, while ensuring all characters of `t` are still present.
    
3. Utilize a character frequency map to keep track of the characters from `t` in the current window.
    

## Efficient Solution

The efficient approach leverages the sliding window technique. Below is the step-by-step explanation of the code:

1. **Initialization**: Create two pointers, `left` and `right`, both initially set to the start of the string `s`. Use two dictionaries, `dict_t` to store the frequency of characters in `t`, and `window_counts` to store the frequency of characters in the current window.
    
2. **Expand the Window**: Move the `right` pointer to expand the window, adding characters to `window_counts`. Keep track of how many target characters have been fully matched.
    
3. **Contract the Window**: Once all characters from `t` are in the current window, attempt to minimize the window by moving the `left` pointer to the right. Update the result whenever a smaller valid window is found.
    
4. **Update the Result**: Throughout the process, maintain variables to store the minimum window's length and its position.
    

Here's the solution code based on the provided efficient approach:

```python
from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    # Count all characters in t
    dict_t = Counter(t)
    required = len(dict_t)

    # Use two pointers to create the sliding window
    left, right = 0, 0
    formed = 0
    window_counts = defaultdict(int)
    min_len = float("inf")
    min_left, min_right = 0, 0

    while right < len(s):
        char = s[right]
        window_counts[char] += 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]

            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left, min_right = left, right

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            left += 1

        right += 1

    return "" if min_len == float("inf") else s[min_left:min_right + 1]
```

In this solution, we use a sliding window approach to efficiently track the required characters. The dictionary `window_counts` keeps track of how many times a character appears in the current window, while `formed` ensures that all characters in `t` are fully present. The outer loop moves the `right` pointer to expand the window, and the inner loop moves `left` to minimize the window size.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(N + M)`, where `N` is the length of `s` and `M` is the length of `t`. In the worst case, each character of `s` is visited twice by both `left` and `right` pointers, giving us a linear complexity.
    
* **Space Complexity**: The space complexity is `O(N + M)` because we are using dictionaries to store character frequencies from both `s` and `t`. The additional space used is proportional to the number of unique characters in both strings.
    

This efficient solution ensures that we minimize the length of the substring while only expanding or contracting the window as necessary, making it a much better alternative to the brute force approach.

## Conclusion

The "Minimum Window Substring" problem is an excellent example of how an optimized sliding window approach can significantly improve the performance compared to a brute force solution. By carefully expanding and contracting the window, and leveraging character frequency maps, we achieve a time-efficient solution that is well-suited for real-world applications. Mastering this problem helps in honing one's ability to deal with substring-related challenges and sharpens overall problem-solving skills. Remember, understanding when to use the sliding window technique is key to solving many similar problems efficiently. Keep practicing, and you'll find yourself more comfortable with these types of algorithmic challenges.


README for [Minimum Window Substring (Leetcode #76)](https://blog.unwiredlearning.com/minimum-window-substring) was compiled from the Unwired Learning Blog.