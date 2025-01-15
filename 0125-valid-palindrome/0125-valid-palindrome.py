class Solution:
    def is_alphanumeric(self, element):
        """Check if a character is alphanumeric."""
        return ('A' <= element <= 'Z') or ('a' <= element <= 'z') or ('0' <= element <= '9')

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:

            # Increment left pointer if not alphanumeric
            while left < right and not self.is_alphanumeric(s[left]):
                left += 1
                
            # Decrement right pointer if not alphanumeric
            while left < right and not self.is_alphanumeric(s[right]):
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True
    

#Question: https://leetcode.com/problems/valid-palindrome
#Blog: https://blog.unwiredlearning.com/valid-palindrome