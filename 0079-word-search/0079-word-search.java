
public class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0) && dfs(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int i, int j, int k) {
        if (k == word.length()) {
            return true;
        }
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(k)) {
            return false;
        }
        char tmp = board[i][j];
        board[i][j] = '/';
        boolean result = dfs(board, word, i + 1, j, k + 1) ||
                         dfs(board, word, i - 1, j, k + 1) ||
                         dfs(board, word, i, j + 1, k + 1) ||
                         dfs(board, word, i, j - 1, k + 1);
        board[i][j] = tmp;
        return result;
    }
}
