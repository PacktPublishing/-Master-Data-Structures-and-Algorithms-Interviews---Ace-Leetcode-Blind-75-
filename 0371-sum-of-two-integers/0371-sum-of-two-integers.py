class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit integer max value
        MAX = 0x7FFFFFFF
        
        # Mask to get 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            # Calculate the carry bits
            carry = (a & b) & mask
            
            # XOR the bits for sum without carry
            a = (a ^ b) & mask
            
            # Shift the carry to add in the next higher bit position
            b = (carry << 1) & mask
        
        # If a is negative, return a's complement in Python's 32-bit format
        return a if a <= MAX else ~(a ^ mask)


#Question: https://leetcode.com/problems/sum-of-two-integers
#Blog: https://blog.unwiredlearning.com/sum-of-two-integers