class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, j = 0, len(people) - 1
        boats = 0
        
        # Loop until the two pointers meet or cross each other
        while i <= j: 
            boats += 1

            # Check if the lightest and heaviest person can share a boat
            if people[i] + people[j] <= limit:
                i += 1
            
            j -= 1

        # Return the total number of boats used
        return boats
    

#Question: https://leetcode.com/problems/boats-to-save-people
#Blog: https://blog.unwiredlearning.com/boats-to-save-people