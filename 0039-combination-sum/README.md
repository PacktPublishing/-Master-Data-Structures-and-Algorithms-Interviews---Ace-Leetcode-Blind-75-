# Combination Sum (Leetcode #39)

The Combination Sum problem is an interesting challenge from LeetCode that deals with discovering all unique combinations from a given list of numbers that sum up to a specific target value. Let's dive into this problem step by step to understand how to solve it efficiently.

## Understanding the Problem Statement

You are given an array of **candidates**, which contains positive integers, and a **target** value. The goal is to find all unique combinations from the candidates that sum up to the given target value. You may use each number in the candidates list as many times as needed.

To make it clear:

* **Input**: candidates = \[2, 3, 6, 7\], target = 7
    
* **Output**: \[\[7\], \[2, 2, 3\]\]
    

**Rules to Note**:

* The same number may be used multiple times, but each combination should be unique.
    
* The order of elements in a combination does not matter.
    

## Brute Force Approach

The brute force approach to this problem involves generating all possible combinations and checking whether they match the target sum. This solution works by considering each candidate and recursively forming all possible combinations.

**Steps**:

1. Recursively include each element in the current combination.
    
2. Continue the process until the sum of the current combination matches the target or exceeds it.
    
3. If the target is reached, store the combination as a valid result.
    
4. If the sum exceeds the target, discard that combination.
    

This approach works, but it has a high computational cost due to the number of repeated recursive calls and the many combinations generated, including invalid ones. The efficiency of this brute force solution can be further improved by avoiding unnecessary branches.

## Hint to Solve the Problem Efficiently

One of the ways to efficiently solve this problem is by employing **Depth First Search (DFS)** with backtracking. In the provided code, notice the strategic use of recursion combined with selective branching. This helps to reduce the number of combinations that need to be explored.

Here’s a key hint: focus on controlling the recursive function so that it only considers combinations that are **within the constraints** (i.e., the current sum does not exceed the target). This ensures that unnecessary work is eliminated early on, saving computation time.

## Efficient Solution

Below is the Python solution that leverages DFS along with backtracking to find all valid combinations that sum up to the target value:

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        all_combinations = []

        def dfs(index, current_combination, current_sum):

            # If the current sum equals the target, we've found a valid combination.
            if current_sum == target:
                all_combinations.append(current_combination)
                return

            # If we've considered all candidates or the current sum exceeds the target, backtrack.
            if index >= len(candidates) or current_sum > target:
                return
            
            # Include the current candidate and recurse
            dfs(index, current_combination + [candidates[index]], current_sum + candidates[index])
            
            # Move to the next candidate without including the current one
            dfs(index + 1, current_combination, current_sum)

        # Start the DFS with an empty combination and a sum of 0.
        dfs(0, [], 0)
        return all_combinations
```

**Explanation**:

* The `dfs` function is used to perform depth-first search.
    
* The function takes the current index, the current combination, and the current sum as arguments.
    
* We keep adding candidates to the combination while ensuring the sum does not exceed the target.
    
* Backtracking is applied when we either reach a valid solution (sum equals target) or exceed the target, which ensures we explore only viable paths.
    

The main advantage here is that we minimize the number of combinations generated, only exploring the ones that are likely to reach the target.

## Time and Space Complexity

**Time Complexity**: The time complexity is **O(2^n)**, where **n** is the number of elements in the candidates array. This is because, in the worst case, we may need to explore all possible subsets of candidates to find the valid combinations. However, due to pruning of unnecessary branches, the solution is significantly faster than the brute force approach.

**Space Complexity**: The space complexity is **O(target)** due to the recursion stack. The maximum depth of the recursion is determined by how many times we add candidates to reach the target value, so it depends on the size of the target.

## Conclusion

This efficient solution to the Combination Sum problem makes use of DFS and backtracking to intelligently explore potential combinations while minimizing the computational overhead. This method is effective, scalable, and helps in efficiently finding the correct combinations without generating all possible subsets.


README for [Combination Sum (Leetcode #39)](https://blog.unwiredlearning.com/combination-sum) was compiled from the Unwired Learning Blog.