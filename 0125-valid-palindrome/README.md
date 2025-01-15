# Valid Palindrome (Leetcode #125)

In this blog, we will explore how to solve the Leetcode problem '125. Valid Palindrome.' We will start by understanding the problem statement, move through a common brute force approach, provide a hint to guide you towards the efficient solution, and then dive into the efficient solution in detail.

## Understanding the Problem Statement

The problem requires determining if a given string is a **valid palindrome**. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and case.

Given a string `s`, the goal is to check if it is a valid palindrome. To do this, we need to ignore non-alphanumeric characters and consider only letters and numbers. Additionally, letter case should be ignored, meaning `A` should be treated the same as `a`.

For example:

* **Input**: `s = "A man, a plan, a canal: Panama"`
    
* **Output**: `true`
    
* **Input**: `s = "race a car"`
    
* **Output**: `false`
    

## Brute Force Approach

A brute force approach to solve this problem would be as follows:

1. **Filter the String**: Iterate through the string, and add only alphanumeric characters to a new list or string while converting them to lowercase.
    
2. **Check for Palindrome**: Use two pointers, one at the start and one at the end of the new string or list, and check if characters at both ends are equal. If any mismatch is found, return `false`. If the entire iteration completes without finding a mismatch, return `true`.
    

This approach, while easy to understand, is inefficient due to the overhead involved in creating a new string or list with only alphanumeric characters, especially if the given string is very large. Additionally, iterating through the filtered list twice—once for filtering and once for checking—can be time-consuming.

## Hint to Solve the Problem Efficiently

To solve the problem more efficiently, you can use a **two-pointer approach** directly on the original string without creating a separate list of filtered characters. Instead, use two pointers to traverse the string from both ends, skipping non-alphanumeric characters in place. This approach allows you to save time and space.

Think about how you can move the two pointers inward while checking for character equality and skipping irrelevant characters (such as punctuation and spaces).

## Efficient Solution

Let's dive into the efficient solution, based on the provided code:

```python
import re

def isPalindrome(s):
    # Step 1: Initialize two pointers
    left, right = 0, len(s) - 1

    # Step 2: Traverse the string from both ends
    while left < right:
        # Skip non-alphanumeric characters on the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters on the right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters
        if s[left].lower() != s[right].lower():
            return False
        
        # Move both pointers inward
        left += 1
        right -= 1
    
    return True
```

**Step-by-Step Explanation**:

1. **Initialize Two Pointers**: Set up two pointers, `left` and `right`, to start from the beginning and end of the string, respectively. This allows you to compare characters from both ends.
    
    ```python
    left, right = 0, len(s) - 1
    ```
    
2. **Skip Non-Alphanumeric Characters**: As you traverse the string, skip any character that is not alphanumeric. This is done using a while loop for both `left` and `right` pointers. This ensures that only letters and numbers are considered.
    
    ```python
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1
    ```
    
3. **Compare Characters**: Convert both characters to lowercase and compare them. If a mismatch is found, return `False`. Otherwise, continue moving both pointers inward.
    
    ```python
    if s[left].lower() != s[right].lower():
        return False
    
    left += 1
    right -= 1
    ```
    
4. **Return True**: If the pointers have successfully crossed each other without finding a mismatch, the string is a valid palindrome, and `True` is returned.
    
    ```python
    return True
    ```
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is `O(n)`, where `n` is the length of the string. This is because each character in the string is processed at most once, and the two-pointer approach ensures that we traverse the string in a single pass.
    
* **Space Complexity**: The space complexity is `O(1)`, since we are using only a constant amount of extra space (the two pointers). Unlike the brute force approach, we are not creating an additional string or list to store the filtered characters.
    

## Conclusion

The efficient solution to determine if a given string is a valid palindrome uses a two-pointer approach to traverse the string from both ends, skipping irrelevant characters, and comparing the alphanumeric characters directly. This approach is optimal in terms of both time and space, making it ideal for large input strings where efficiency is crucial.


README for [Valid Palindrome (Leetcode #125)](https://blog.unwiredlearning.com/valid-palindrome) was compiled from the Unwired Learning Blog.