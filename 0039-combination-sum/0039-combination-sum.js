
function combinationSum(candidates, target) {
    let allCombinations = [];
    
    function dfs(index, currentCombination, currentSum) {
        if (currentSum === target) {
            allCombinations.push([...currentCombination]);
            return;
        }

        if (index >= candidates.length || currentSum > target) {
            return;
        }

        // Include the current candidate
        currentCombination.push(candidates[index]);
        dfs(index, currentCombination, currentSum + candidates[index]);
        currentCombination.pop();

        // Move to the next candidate without including the current one
        dfs(index + 1, currentCombination, currentSum);
    }

    dfs(0, [], 0);
    return allCombinations;
}
