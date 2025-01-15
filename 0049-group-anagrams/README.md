# Group Anagrams (Leetcode #49)

Anagrams are words or phrases formed by rearranging the letters of another, using all the original letters exactly once. In Leetcode Problem 49, you're asked to group an array of strings into collections where each group contains anagrams.

## Understanding the Problem Statement

The problem is stated as follows: Given an array of strings, group the anagrams together.

**Example:**

Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

Output: `[ ["eat", "tea", "ate"], ["tan", "nat"], ["bat"] ]`

Each group contains words that are anagrams of each other. Note that the order within each group or the groups themselves does not matter.

## Brute Force Approach

The brute force approach is to compare each word with every other word to check if they are anagrams. This inggvolves sorting each word and comparing its sorted version with others, which allows us to determine if they match.

**Steps:**

1. For each word in the array, sort its letters.
    
2. Compare the sorted version with other words.
    
3. Group words with the same sorted version.
    

The brute force method is inefficient because sorting each word takes `O(L log L)` time, and comparing all possible pairs has a time complexity of `O(N^2)`. Thus, this approach can become very slow for large inputs.

## Hint to Solve the Problem Efficiently

The hint for an efficient solution is to use a hash map to avoid redundant comparisons. Instead of sorting each word, you can use a different characteristic that uniquely represents anagrams. Specifically, you can use character counts as keys in a dictionary to keep track of words that are anagrams.

## Efficient Solution

The provided code takes advantage of hashing to group anagrams efficiently.

**Steps of the Efficient Solution:**

1. Create an empty dictionary (`anagram_map`) where each key is a unique representation of a group of anagrams.
    
2. Iterate over each word in the input list:
    
    * For each word, create a list of 26 zeros representing the character count for each letter in the alphabet (since we're only dealing with lowercase English letters).
        
    * Update the character count for each letter in the word.
        
    * Convert the character count list into a tuple and use it as a key in the dictionary.
        
    * Append the word to the list corresponding to that key.
        
3. Return the values of the dictionary as the result.
    

Here's a simplified version of the efficient code:

```plaintext
from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Create a count of 26 zeros for each letter in the alphabet
        count = [0] * 26
        
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        # Use the tuple of counts as the key
        anagram_map[tuple(count)].append(word)
    
    return list(anagram_map.values())
```

**Explanation:**

* We use a list of size 26 to count the frequency of each letter in a word. This list is then converted to a tuple so it can be used as a key in the dictionary (`anagram_map`).
    
* The dictionary (`anagram_map`) stores lists of words that are anagrams, indexed by their character count.
    
* Finally, the result is the list of all the values in the dictionary.
    

## Time and Space Complexity

**Time Complexity:**

* Constructing the character count list for each word takes `O(L)`, where `L` is the length of the word.
    
* Iterating over all `N` words in the input list takes `O(N * L)` time, where `N` is the number of words and `L` is the average length of the words.
    
* Thus, the overall time complexity is `O(N * L)`.
    

**Space Complexity:**

* We use a dictionary to store the groups of anagrams. In the worst case, every word could be an anagram of every other word, leading to `O(N * L)` space for the dictionary.
    
* Additionally, we use `O(N * L)` space for storing the character counts as keys in the dictionary.
    
* Thus, the overall space complexity is `O(N * L)`.
    

This solution is significantly more efficient than the brute force approach because it avoids repeatedly sorting strings and instead uses a fixed-size representation for each word, making it suitable for large inputs.

## Conclusion

Leetcode Problem 49, Group Anagrams, is a great example of how to use hashing to solve problems more efficiently. The brute force approach of sorting each word and comparing is impractical for large datasets, whereas using character counts as keys in a hash map provides an elegant and efficient solution. By understanding the properties of anagrams and leveraging data structures like dictionaries, you can solve this problem in `O(N * L)` time complexity, which is well-suited for larger inputs. This approach highlights the importance of choosing the right data representation and algorithm to achieve optimal performance.


README for [Group Anagrams (Leetcode #49)](https://blog.unwiredlearning.com/group-anagram) was compiled from the Unwired Learning Blog.