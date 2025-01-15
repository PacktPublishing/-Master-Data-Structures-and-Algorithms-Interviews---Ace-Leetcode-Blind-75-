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
            
            dfs(index, current_combination + [candidates[index]], current_sum + candidates[index])
            dfs(index + 1, current_combination, current_sum)

        # Start the DFS with an empty combination and a sum of 0.
        dfs(0, [], 0)
        return all_combinations


#Question: https://leetcode.com/problems/combination-sum
#Blog: https://blog.unwiredlearning.com/combination-sum