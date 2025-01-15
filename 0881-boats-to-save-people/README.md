# Boats to Save People  (Leetcode #881)

In today's blog, we will explore the solution to a popular Leetcode problem - **881\. Boats to Save People**. This is a classic problem involving a mix of logic and optimization, often encountered in real-world rescue scenarios. We'll walk through the problem statement, consider a brute force approach, provide a useful hint, and finally discuss an efficient solution. Let’s dive in!

## Understanding the Problem Statement

The problem at hand is titled **"Boats to Save People"**. Imagine that you are managing a rescue operation, and you have a group of people with different weights, and a set of boats. Each boat has a maximum weight limit, and can hold at most two people. You need to determine the minimum number of boats required to rescue all the people.

The problem asks you to implement a function, which takes in:

1. A list of integers representing the weights of people.
    
2. An integer representing the weight limit of each boat.
    

The goal is to find out how many boats are needed to rescue all the people, given the weight limitations.

## Brute Force Approach

A common brute force approach would be to iterate through all possible pairs of people and find a combination of pairs that minimizes the number of boats used. This means checking each possible pair, seeing if they can fit in a boat, and repeating until all people are accounted for. While this approach works for small inputs, it becomes computationally expensive for larger lists, as the number of combinations grows rapidly.

The brute force method is simply too slow for larger datasets, leading us to search for a more efficient solution.

## Hint to Solve the Problem Efficiently

If you look closely at the problem, you will notice that pairing the heaviest person who is not yet in a boat with the lightest person available might often be the optimal way to minimize the number of boats. This way, we try to make the most efficient use of the boat's weight capacity, reducing the total number of trips needed.

## Efficient Solution

The provided solution leverages a **two-pointer technique** to optimize the pairing process. Here’s a step-by-step explanation of how it works:

```python
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
```

In this solution:

1. **Sorting**: First, we sort the list of people's weights in ascending order.
    
2. **Two Pointers**: We use two pointers, `i` starting from the lightest person (beginning of the list), and `j` starting from the heaviest person (end of the list).
    
3. **Boat Allocation**: We then try to pair the lightest and heaviest person together. If their combined weight is within the boat's limit, we increase `i` and move to the next lightest person. In either case, we always decrease `j` to account for the heaviest person.
    
4. **Count Boats**: Each iteration represents one boat being used, and the process continues until all people are assigned boats.
    

This approach ensures that we are making the most efficient pairing possible, minimizing the total number of boats.

## Time and Space Complexity

* **Time Complexity**: The time complexity of this solution is **O(n log n)**, where `n` is the number of people. This complexity comes from the initial sorting step, followed by a linear pass through the list using the two pointers.
    
* **Space Complexity**: The space complexity is **O(1)** if we consider the input list being sorted in place, or **O(n)** if the sorting algorithm requires additional space.
    

## Conclusion

The problem of **Boats to Save People** is an interesting challenge that requires both logical pairing and efficient problem-solving skills. The brute force method is good for understanding the problem, but using the two-pointer technique gives us a much more scalable solution. By sorting the people and carefully pairing the lightest and heaviest individuals, we can significantly reduce the number of boats needed.

We hope this explanation helped you understand how to solve this problem efficiently. Practice applying these techniques to similar problems, and you’ll get better at optimizing your solutions over time!

README for [Boats to Save People  (Leetcode #881)](https://blog.unwiredlearning.com/boats-to-save-people) was compiled from the Unwired Learning Blog.