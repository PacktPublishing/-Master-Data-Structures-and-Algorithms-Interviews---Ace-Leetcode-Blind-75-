class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize a list to store the result
        result = [0] * (n + 1)
        
        # If n is 0, simply return the result list (which is [0])
        if n == 0:
            return result
        
        # The number of 1's in the binary representation of 1 is 1
        result[1] = 1
        
        # Loop through numbers from 2 to n
        for i in range(2, n + 1):
            if i % 2 == 0:
                result[i] = result[i // 2]
            else: 
                result[i] = result[i // 2] + 1
        
        return result
    

#Question: https://leetcode.com/problems/counting-bits
#Blog: https://blog.unwiredlearning.com/counting-bits