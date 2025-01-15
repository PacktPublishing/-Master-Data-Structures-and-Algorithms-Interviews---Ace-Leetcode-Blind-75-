class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Depth First Search (DFS) function to mark visited land
        def dfs(i, j):
            # Base case: if the index is out of bounds or the cell is water ('0'), return
            if (i < 0 or i >= len(grid) or 
                j < 0 or j >= len(grid[0]) or grid[i][j] == '0'):
                return
                
            grid[i][j] = '0'  # Mark as visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0

        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count
    
    
#Question: https://leetcode.com/problems/number-of-islands
#Blog: https://blog.unwiredlearning.com/number-of-islands