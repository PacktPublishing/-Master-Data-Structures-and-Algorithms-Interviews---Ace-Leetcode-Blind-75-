# Valid Anagram (Leetcode #242)

When tackling coding challenges, the "Valid Anagram" problem is an excellent way to understand strings and hashmaps better. Let's dive into the problem, explore different approaches, and break down an efficient solution step-by-step.

## Understanding the Problem Statement

The problem statement is:

> Given two strings, `s` and `t`, determine if `t` is an anagram of `s`.

An **anagram** is a word formed by rearranging the letters of a different word, using all the original letters exactly once. For instance, "listen" is an anagram of "silent".

The function should return `True` if the strings `s` and `t` are anagrams, and `False` otherwise.

**Example:**

* Input: `s = "anagram"`, `t = "nagaram"`
    
* Output: `True`
    
* Input: `s = "rat"`, `t = "car"`
    
* Output: `False`
    

## Brute Force Approach

A common brute force approach to solve this problem would be:

* **Sort the Strings**: Sort both strings `s` and `t`. If both sorted strings are equal, then `t` is an anagram of `s`.
    
* **Comparison**: Compare the two sorted strings to determine if they match.
    

**Code:**

```plaintext
s_sorted = sorted(s)
t_sorted = sorted(t)
return s_sorted == t_sorted
```

**Time Complexity**: The brute force approach requires sorting the strings, which would take **O(n log n)** time, where `n` is the length of the strings. Sorting is a common and straightforward way to solve the problem, but it is not the most efficient.

## Hint to Solve the Problem Efficiently

Think about **counting the frequency** of each character in both strings. If the character counts match, then the strings are anagrams. Using a hashmap or an array to track character frequencies can significantly improve the efficiency of the solution.

## Efficient Solution

The efficient way to solve this problem involves using a **hashmap (dictionary in Python)** to count the frequency of each character in both strings `s` and `t`. Here's how it can be done:

1. If the lengths of `s` and `t` are not the same, immediately return `False`. Two strings of different lengths cannot be anagrams.
    
2. Use a hashmap to count the occurrence of each character in `s`.
    
3. Decrement the count for each character found in `t`.
    
4. If any character count does not match, return `False`. Otherwise, return `True`.
    

**Code:**

```plaintext
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    # Count the frequency of characters in s
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Decrement the frequency based on characters in t
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True
```

## Time and Space Complexity

* **Time Complexity**: **O(n)**, where `n` is the length of the strings `s` and `t`. The solution iterates over each character in `s` and `t` exactly once.
    
* **Space Complexity**: **O(1)** (considering constant space usage) or **O(k)**, where `k` is the number of unique characters in the input alphabet. Since we are storing character frequencies, the hashmap size will be proportional to the number of unique characters. In most scenarios involving only lowercase English letters, this space requirement is effectively constant.
    

## Conclusion

While the brute force solution sorts the strings, the efficient solution leverages a character frequency count, making it a linear-time approach. This type of problem highlights the importance of evaluating both time and space complexity to find an optimal solution, especially for larger inputs.

Use this efficient approach to ace the "Valid Anagram" question on LeetCode and understand the power of hashmaps in string problems!


README for [Valid Anagram (Leetcode #242)](https://blog.unwiredlearning.com/valid-anagram) was compiled from the Unwired Learning Blog.