class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:

    # Function to build a Trie from the given list of words
    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
        return root

    # Depth-first search function to find words in the board
    def dfs(self, board, node, i, j, path, result):
        if node.is_end:
            result.add(path)
            node.is_end = False  # Avoid duplicates
        
        # Boundary conditions and character check
        if (i < 0 or i >= len(board) or 
            j < 0 or j >= len(board[0]) or 
            board[i][j] not in node.children):
            return
        temp, board[i][j] = board[i][j], '#'  # Mark as visited
        
        # Explore all four possible directions
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            self.dfs(board, node.children[temp], x, y, path + temp, result)
        board[i][j] = temp  # Unmark
    
    # Main function to find all words in the board
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.buildTrie(words)
        result = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self.dfs(board, root, i, j, '', result)
        return list(result)
    

#Question: https://leetcode.com/problems/word-search-ii
#Blog: https://blog.unwiredlearning.com/word-search-ii