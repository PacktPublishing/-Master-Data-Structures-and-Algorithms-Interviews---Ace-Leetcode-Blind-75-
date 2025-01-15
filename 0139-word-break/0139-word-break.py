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
        

#Question: https://leetcode.com/problems/word-break
#Blog: https://blog.unwiredlearning.com/word-break