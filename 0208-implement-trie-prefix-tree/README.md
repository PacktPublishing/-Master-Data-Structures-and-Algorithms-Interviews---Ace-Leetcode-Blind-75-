# Implement Trie (Prefix Tree) (Leetcode #208)

Tries, also known as Prefix Trees, are an important data structure used to efficiently store and search collections of strings. They are particularly useful when dealing with scenarios that involve prefix-based searching, such as autocomplete systems. In this blog, we will explore how to implement a Trie for solving Leetcode Problem 208, which involves creating an efficient data structure that can perform insert, search, and prefix operations on words.

## Understanding the Problem Statement

The problem asks you to implement a data structure called a Trie, also known as a Prefix Tree. A Trie is used to store a collection of strings, primarily to support efficient prefix searches. You need to design three primary functions:

* **Insert** a word into the Trie.
    
* **Search** if a word exists in the Trie.
    
* **startsWith** to determine if any word in the Trie starts with a given prefix.
    

For example, inserting "cat", "cap", and "dog" will store all these words in such a way that the shared characters can be used to optimize space. Searching for "cap" will return true, while searching for "car" will return false.

## Brute Force Approach

A brute force way to implement this problem is by using an array or a list to store all the words. For each search operation, you would iterate through the entire list, checking each word until you find a match or exhaust the list. Similarly, for the prefix operation, you would need to iterate through every word, checking if it begins with the desired prefix.

While this approach is simple to implement, it becomes inefficient when the dataset grows larger. The search and prefix operations have a time complexity of **O(n × m)**, where **n** is the number of words and **m** is the average length of the words, making this approach slow for large datasets.

## Hint to Solve the Problem Efficiently

Instead of storing individual words, think of storing the words in a hierarchical structure, where each character represents a node. This hierarchical structure would allow you to share prefixes between words, thus reducing redundancy. Each node should keep track of its children and whether it is the end of a word.

## Efficient Solution

A more efficient approach is to use a Trie, which is a tree-like data structure where each node represents a character. The provided code efficiently implements this solution:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

The **TrieNode** class represents each node of the Trie, containing a dictionary of children and a flag to indicate the end of a word.

The **Trie** class has three functions:

* **insert(word)**: Iterates through each character in the word, and either traverses or creates a new node in the children dictionary for each character. Finally, it marks the end of the word.
    
* **search(word)**: Checks if the word exists by traversing through each character, returning **True** if the final node is marked as the end.
    
* **startsWith(prefix)**: Checks if a given prefix exists by traversing each character, returning **True** if all characters are found.
    

## Time and Space Complexity

* **Insert Operation**: The time complexity is **O(m)**, where **m** is the length of the word to be inserted. Each character of the word is processed only once.
    
* **Search Operation**: The time complexity is also **O(m)**, where **m** is the length of the word. We traverse each character to check if the word exists.
    
* **startsWith Operation**: Similarly, the time complexity is **O(m)**, where **m** is the length of the prefix.
    

The space complexity for the Trie is **O(n × m)**, where **n** is the number of words and **m** is the average length of each word. Each node may have multiple children, resulting in an overall space usage that depends on the size of the input dataset. However, this structure is still efficient compared to storing individual words, especially when words share prefixes.

## Conclusion

Implementing a Trie is an efficient way to handle prefix-based searches and can significantly improve performance compared to brute force methods. Tries are widely used in applications like search engines, autocomplete systems, and dictionaries, where fast retrieval of words or prefixes is critical. By breaking down words into individual characters and organizing them in a hierarchical structure, Tries help reduce redundancy and optimize search operations. Hopefully, this guide has helped you understand how to implement a Trie and leverage it effectively to solve Leetcode Problem 208.


README for [Implement Trie (Prefix Tree) (Leetcode #208)](https://blog.unwiredlearning.com/implement-trie-prefix-tree) was compiled from the Unwired Learning Blog.