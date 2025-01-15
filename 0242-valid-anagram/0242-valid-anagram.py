class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        # Convert both to lowercase to ignore case match
        str1 = str1.lower()
        str2 = str2.lower()

        # Strip off all the white spaces
        str1 = str1.replace(" ", "")
        str2 = str2.replace(" ", "")

        # Initialize the bucket array
        counts = [0] * 26

        # Fill the buckets
        for char in str1:
            counts[ord(char) - ord('a')] += 1

        # Empty the buckets
        for char in str2:
            counts[ord(char) - ord('a')] -= 1

        # Check if all buckets are empty
        for count in counts:
            if count != 0:
                return False

        return True


#Question: https://leetcode.com/problems/valid-anagram
#Blog: https://blog.unwiredlearning.com/valid-anagram