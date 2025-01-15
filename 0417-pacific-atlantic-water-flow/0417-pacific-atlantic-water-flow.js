var pacificAtlantic = function(heights) {
    if (!heights || heights.length === 0) {
        return [];
    }

    const m = heights.length, n = heights[0].length;
    const pacificReachable = Array.from({ length: m }, () => Array(n).fill(false));
    const atlanticReachable = Array.from({ length: m }, () => Array(n).fill(false));

    const dfs = (row, col, reachable) => {
        reachable[row][col] = true;
        const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];

        for (let [dr, dc] of directions) {
            const newRow = row + dr, newCol = col + dc;
            if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n &&
                !reachable[newRow][newCol] && heights[newRow][newCol] >= heights[row][col]) {
                dfs(newRow, newCol, reachable);
            }
        }
    };

    for (let i = 0; i < m; i++) {
        dfs(i, 0, pacificReachable);
        dfs(i, n - 1, atlanticReachable);
    }

    for (let j = 0; j < n; j++) {
        dfs(0, j, pacificReachable);
        dfs(m - 1, j, atlanticReachable);
    }

    const result = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (pacificReachable[i][j] && atlanticReachable[i][j]) {
                result.push([i, j]);
            }
        }
    }

    return result;
};
