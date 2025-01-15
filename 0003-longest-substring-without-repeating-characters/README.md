 # Longest Substring Without Repeating Characters (Leetcode #3)
 
 The 'Longest Substring Without Repeating Characters' is one of Leetcode's classic problems that tests your understanding of efficient string manipulation. Let's walk through the problem step-by-step, explore both brute force and efficient solutions, and see how we can arrive at the best approach.

## Understanding the Problem Statement

The problem asks us to find the length of the longest substring without repeating characters in a given string. A substring is defined as a contiguous sequence of characters within a string. For example, given the string **s = "abcabcbb"**, the answer is **3**, since the longest substring without repeating characters is **"abc"**.

The challenge here is to efficiently determine this length while avoiding unnecessary operations, especially as the string size grows.

## Brute Force Approach

The brute force solution to this problem involves generating all possible substrings and checking each one for repeated characters. We can summarize the brute force approach in the following steps:

1. Start by iterating through each character in the string.
    
2. For each character, create all possible substrings starting from that character.
    
3. Check if the current substring has all unique characters.
    
4. Track the maximum length of the substrings without any repeating characters.
    

Although conceptually simple, this method is highly inefficient for long strings because it involves examining multiple overlapping substrings. The time complexity of this approach is **O(n^3)** since generating substrings and verifying uniqueness both require substantial operations.

## Hint to Solve the Problem Efficiently

Instead of generating all substrings, consider the possibility of sliding a window across the string to dynamically track the longest substring without repeating characters. You can think of this "window" as a way of expanding and shrinking the range of characters you are examining.

To solve the problem efficiently, you will need to:

1. Maintain a record of the characters you have seen, along with their positions.
    
2. Adjust the window when you encounter a repeating character to ensure it only includes unique characters.
    

## Efficient Solution

The most efficient solution to this problem is achieved using the **Sliding Window** technique along with a **HashMap** (or dictionary). The idea is to maintain two pointers, a left and a right pointer, which represent the current window of unique characters. Here is the step-by-step solution based on the uploaded code:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1
            
            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
```

In this solution:

1. **char\_index\_map** is a dictionary that stores the index of each character in the string.
    
2. **left** and **right** pointers represent the current window of unique characters.
    
3. As you iterate with **right**, whenever you encounter a character that is already in the window (i.e., between **left** and **right** pointers), you adjust the **left** pointer to exclude the repeated character.
    
4. Finally, you compute the maximum window length (**max\_length**) as you go along.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of the above solution is **O(n)**, where **n** is the length of the string. Each character is visited only once, thanks to the sliding window approach, making this solution efficient.
    
* **Space Complexity**: The space complexity is **O(min(n, m))**, where **n** is the length of the string and **m** is the size of the character set (e.g., 26 for lowercase alphabets). We use additional space to store character indices in **char\_index\_map**.
    

## Conclusion

The **Sliding Window** approach provides an optimal solution for the "Longest Substring Without Repeating Characters" problem by reducing redundant operations and ensuring each character is processed only once. This method is ideal for balancing both time and space efficiency compared to the brute force approach.


README for [Longest Substring Without Repeating Characters (Leetcode #3)](https://blog.unwiredlearning.com/longest-substring-without-repeating-characters) was compiled from the Unwired Learning Blog.