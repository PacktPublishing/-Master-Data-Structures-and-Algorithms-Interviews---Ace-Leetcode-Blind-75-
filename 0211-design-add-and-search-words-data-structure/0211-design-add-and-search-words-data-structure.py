class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

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


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


#Question: https://leetcode.com/problems/design-add-and-search-words-data-structure
#Blog: https://blog.unwiredlearning.com/design-add-and-search-words-data-structure