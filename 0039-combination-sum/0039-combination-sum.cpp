
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> allCombinations;
        vector<int> currentCombination;
        dfs(candidates, 0, target, currentCombination, allCombinations);
        return allCombinations;
    }

private:
    void dfs(vector<int>& candidates, int index, int target, vector<int>& currentCombination, vector<vector<int>>& allCombinations) {
        if (target == 0) {
            allCombinations.push_back(currentCombination);
            return;
        }

        if (index >= candidates.size() || target < 0) {
            return;
        }

        // Include the current candidate
        currentCombination.push_back(candidates[index]);
        dfs(candidates, index, target - candidates[index], currentCombination, allCombinations);
        currentCombination.pop_back();

        // Move to the next candidate without including the current one
        dfs(candidates, index + 1, target, currentCombination, allCombinations);
    }
};
