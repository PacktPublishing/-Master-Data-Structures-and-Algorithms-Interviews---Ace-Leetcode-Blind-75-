class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Edge case: if the input is empty, return an empty list
        if not heights:
            return []
        
        # Get the dimensions of the matrix
        m, n = len(heights), len(heights[0])
        
        # Initialize matrices to track cells reachable to the Pacific and Atlantic oceans
        pacificReachable = [[False for _ in range(n)] for _ in range(m)]
        atlanticReachable = [[False for _ in range(n)] for _ in range(m)]
        
        # Define the DFS function that marks reachable cells
        def dfs(row, col, reachable):
            # Mark the current cell as reachable for the current ocean
            reachable[row][col] = True
            
            # Define the possible directions to move (up, down, left, right)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dr, dc in directions:
                # Calculate the new cell's position
                newRow, newCol = row + dr, col + dc
                
                # Check if the new cell is within bounds, unvisited, and its height is >= current cell's height
                if (0 <= newRow < m and 0 <= newCol < n and not reachable[newRow][newCol] and 
                heights[newRow][newCol] >= heights[row][col]):
                    # Recursively perform DFS from the new cell
                    dfs(newRow, newCol, reachable)
        
        # Perform DFS from all cells adjacent to the Pacific ocean
        for i in range(m):
            dfs(i, 0, pacificReachable)
            dfs(i, n - 1, atlanticReachable)
        
        # Perform DFS from all cells adjacent to the Atlantic ocean
        for j in range(n):
            dfs(0, j, pacificReachable)
            dfs(m - 1, j, atlanticReachable)

        print(pacificReachable)
        print(atlanticReachable)
        
        # Collect and return the cells that can reach both oceans
        result = []
        
        for i in range(m):
            for j in range(n):
                if pacificReachable[i][j] and atlanticReachable[i][j]:
                    result.append([i, j])
        
        return result
    

#Question: https://leetcode.com/problems/pacific-atlantic-water-flow
#Blog: https://blog.unwiredlearning.com/pacific-atlantic-water-flow