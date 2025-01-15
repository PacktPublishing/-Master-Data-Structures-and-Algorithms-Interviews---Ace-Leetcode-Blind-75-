import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        if (heights == null || heights.length == 0) {
            return result;
        }

        int m = heights.length;
        int n = heights[0].length;
        boolean[][] pacificReachable = new boolean[m][n];
        boolean[][] atlanticReachable = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            dfs(heights, pacificReachable, i, 0);
            dfs(heights, atlanticReachable, i, n - 1);
        }

        for (int j = 0; j < n; j++) {
            dfs(heights, pacificReachable, 0, j);
            dfs(heights, atlanticReachable, m - 1, j);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacificReachable[i][j] && atlanticReachable[i][j]) {
                    List<Integer> cell = new ArrayList<>();
                    cell.add(i);
                    cell.add(j);
                    result.add(cell);
                }
            }
        }

        return result;
    }

    private void dfs(int[][] heights, boolean[][] reachable, int row, int col) {
        reachable[row][col] = true;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int[] direction : directions) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            if (newRow >= 0 && newRow < heights.length && newCol >= 0 && newCol < heights[0].length &&
                !reachable[newRow][newCol] && heights[newRow][newCol] >= heights[row][col]) {
                dfs(heights, reachable, newRow, newCol);
            }
        }
    }
}
