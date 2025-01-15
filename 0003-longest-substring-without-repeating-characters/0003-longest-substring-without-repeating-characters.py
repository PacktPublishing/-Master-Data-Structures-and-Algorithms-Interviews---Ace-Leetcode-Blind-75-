class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                
        # Initialize the pointers and the set
        start, end, maxLength = 0, 0, 0
        charSet = set()
        
        while end < len(s):
            if s[end] not in charSet:
                charSet.add(s[end])
                maxLength = max(maxLength, end - start + 1)
                end += 1
            else:
                charSet.remove(s[start])
                start += 1
                
        return maxLength


#Question: https://leetcode.com/problems/longest-substring-without-repeating-characters
#Blog: https://blog.unwiredlearning.com/longest-substring-without-repeating-characters