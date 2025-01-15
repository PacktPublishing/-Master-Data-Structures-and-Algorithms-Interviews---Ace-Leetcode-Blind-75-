class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # Assuming a 32-bit integer
        for _ in range(32):  
            # Check the LSB
            count = count + (n & 1) 

            # Right shift the bits of n
            n = n >> 1                

        return count
    
    
#Question: https://leetcode.com/problems/number-of-1-bits
#Blog: https://blog.unwiredlearning.com/number-of-1-bits