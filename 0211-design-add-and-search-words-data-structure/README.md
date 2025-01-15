# Design Add and Search Words Data Structure (Leetcode #211)

Designing a data structure that can handle adding words and searching with wildcards is an interesting challenge that tests your understanding of tries and recursive search techniques. Let’s solve the LeetCode problem "211. Design Add and Search Words Data Structure" step by step.

## Understanding the Problem Statement

The challenge requires you to create a data structure that supports:

1. **addWord(word)** - Adds a word into the data structure.
    
2. **search(word)** - Searches for a word that may contain the special wildcard character `'.'`. The `'.'` wildcard can match any letter.
    

Consider this example:

* **addWord("chat")**
    
* **search("chat")** returns `true` since the word was added.
    
* **search("ch.t")** returns `true` since the wildcard character `'.'` can match `'a'`.
    
* **search("bat")** returns `false` since this word was never added.
    

Your task is to implement a structure that efficiently supports these operations.

## Brute Force Approach

A brute force approach might be to store all the words in a list and iterate through the list to find matching words whenever a search request is made. This approach would involve a character-by-character comparison and extra logic to handle the wildcard `'.'`, effectively leading to a lot of redundant computations. It becomes highly inefficient when dealing with a large number of words.

**Complexity of the Brute Force Approach**

The time complexity of this brute force approach would be **O(N \* L)**, where **N** is the number of words stored and **L** is the average length of the words. The search operation is especially costly, as it requires iterating over all stored words.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, think of using a **Trie** data structure. A Trie, or prefix tree, provides an efficient way to store words and facilitates fast lookups. In addition, a recursive Depth First Search (DFS) can be used to navigate through the Trie nodes to handle wildcard searches.

## Efficient Solution

The given code leverages a Trie to store words and recursively searches through nodes to handle the wildcard character. Here's how the solution works:

**TrieNode Class**

The `TrieNode` class represents individual nodes in the Trie. Each node has a dictionary called `children` to store references to child nodes and a boolean `is_end` to mark the end of a word.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

**WordDictionary Class**

The `WordDictionary` class handles adding and searching words:

1. **addWord(word)** - This function iterates through the characters in the word and adds them to the Trie, creating new nodes as necessary. The end of the word is marked by setting `is_end` to `True`.
    
2. **search(word)** - This function uses Depth First Search (DFS) to search for the word, handling the wildcard character `'.'` by exploring all possible child nodes.
    

```python
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True        
        
    def search(self, word: str) -> bool:
        node = self.root

        def dfs(node, i):
            if i == len(word):
                return node.is_end
                
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            return False

        return dfs(node, 0)        
```

**How the Wildcard is Handled**

The key part of this solution is how the `'.'` character is handled in the `dfs()` function. When `'.'` is encountered, the algorithm iterates through all the children of the current node, recursively searching each child. This allows the `'.'` to match any character effectively.

## Time and Space Complexity

**Time Complexity**

* **addWord(word)**: The time complexity for adding a word is **O(L)**, where **L** is the length of the word. This is because we need to iterate through all characters of the word to add it to the Trie.
    
* **search(word)**: The time complexity for searching is **O(N)** in the worst case, where **N** is the total number of nodes in the Trie. This happens when using the wildcard character `'.'` and every node must be explored.
    

**Space Complexity**

The space complexity is **O(N \* L)**, where **N** is the number of words and **L** is the average length of the words. Each character in each word needs its own TrieNode, which leads to this complexity.

## Conclusion

This problem provides a great opportunity to understand the power of Tries in efficiently managing word-based data structures, particularly when wildcard searches are involved. By using a Trie and a recursive DFS approach, we can implement the `addWord` and `search` functions in a way that is both time-efficient and space-efficient for large datasets.


README for [Design Add and Search Words Data Structure (Leetcode #211)](https://blog.unwiredlearning.com/design-add-and-search-words-data-structure) was compiled from the Unwired Learning Blog.