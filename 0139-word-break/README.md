# Word Break (Leetcode #139)

The Word Break problem is a classic challenge in dynamic programming and string manipulation that comes up frequently during technical interviews. It tests your ability to segment strings effectively using a given set of words. In this blog, we will dive into solving the Word Break problem, covering a brute force approach, an efficient solution, and analyzing their respective complexities.

## Understanding the Problem Statement

The Word Break problem asks if a given string (`s`) can be segmented into space-separated sequences of one or more dictionary words. Given an input string and a dictionary of words, the goal is to determine if the entire string can be split such that every segment is present in the dictionary.

For example:

* **Input:**
    
    * `s = "leetcode"`
        
    * `wordDict = ["leet", "code"]`
        
* **Output:** `true`
    
* **Explanation:** `"leetcode"` can be segmented as `"leet code"` which are both words present in the dictionary.
    

The problem requires checking all possible segmentations of the string, making it an interesting problem for exploring both brute force and optimized techniques.

## Brute Force Approach

A common approach to solve this problem is through **recursion**. In the brute force solution, we attempt to partition the string in all possible ways and check if each substring exists in the dictionary. Here is a high-level overview of how a brute force solution would work:

1. Start with the first character of the string.
    
2. Incrementally form substrings and check if each substring exists in the given word dictionary.
    
3. Recur for the remaining part of the string if a valid segment is found.
    

This approach is straightforward but highly inefficient due to repeated calculations and overlapping subproblems. As the length of the string increases, the time complexity becomes exponential, which is impractical for large inputs.

## Hint to Solve the Problem Efficiently

To solve the problem efficiently, we can use **dynamic programming** to avoid redundant computations. The hint is to use a boolean array where each element represents whether the substring up to that index can be segmented using words from the dictionary.

## Efficient Solution

Below is an efficient solution based on the provided code, which uses dynamic programming to solve the Word Break problem:

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        res = [False] * (len(s) + 1)
        res[0] = True
        
        # Iterate through all positions in the string
        for i in range(len(s) + 1):
            # Check all words in the wordSet
            for word in wordSet:
                if (res[i] and (i + len(word)) <= len(s) and s[i : i + len(word)] in wordSet):
                    res[i + len(word)] = True
        
        return res[-1]
```

**Explanation:**

* The solution uses a dynamic programming array (`res`) of length `len(s) + 1`, where `res[i]` is `True` if the substring `s[:i]` can be segmented using the words in the dictionary.
    
* We initialize `res[0]` to `True` because an empty string can always be segmented.
    
* We iterate through the string, and for each position, we check all words in the dictionary to see if the substring from the current position matches any word and can form a valid segment.
    
* If a match is found, we update the dynamic programming array to reflect that the substring can be segmented.
    
* The result is returned by checking `res[len(s)]`, which indicates if the entire string can be segmented.
    

## Time and Space Complexity

* **Time Complexity:** The time complexity is **O(n \* m)**, where `n` is the length of the string `s` and `m` is the total number of words in the dictionary. For each position in the string, we iterate over all words, and the substring check takes constant time on average due to the use of a hash set.
    
* **Space Complexity:** The space complexity is **O(n)**, where `n` is the length of the string `s`. We use a dynamic programming array of size `n + 1` to store results for each position in the string.
    

## Conclusion

The Word Break problem is a great example of how dynamic programming can be applied to improve efficiency over brute force approaches. By using a DP array and leveraging the set data structure for fast lookups, we can significantly reduce the time required to solve the problem. Understanding these approaches not only helps in solving similar problems in interviews but also strengthens core algorithmic concepts.

Feel free to try different test cases on your own and see how the optimized solution outperforms the naive one. Happy coding!

README for [Word Break (Leetcode #139)](https://blog.unwiredlearning.com/word-break) was compiled from the Unwired Learning Blog.