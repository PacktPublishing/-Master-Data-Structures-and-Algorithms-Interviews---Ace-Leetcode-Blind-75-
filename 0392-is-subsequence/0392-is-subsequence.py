class Solution:
    def isSubsequence(self, str1: str, str2: str) -> bool:
        # Initialize pointers for both strings
        itr1, itr2 = 0, 0
        
        # We can iterate until either of them becomes zero...
        while itr1 < len(str1) and itr2 < len(str2):
            # Compare characters, increment both pointers if same
            if str1[itr1] == str2[itr2]:
                itr1 += 1
                itr2 += 1
            else:
                itr2 += 1  # Only increment second pointer

        # If it is a subsequence, 'i' will have travelled full
        # length of string 'str1', so just check and return
        return itr1 == len(str1)


#Question: https://leetcode.com/problems/is-subsequence
#Blog: https://blog.unwiredlearning.com/is-subsequence