
var exist = function(board, word) {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j] === word[0] && dfs(board, word, i, j, 0)) {
                return true;
            }
        }
    }
    return false;
};

function dfs(board, word, i, j, k) {
    if (k === word.length) {
        return true;
    }
    if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] !== word[k]) {
        return false;
    }
    let temp = board[i][j];
    board[i][j] = '/';
    let result = dfs(board, word, i + 1, j, k + 1) ||
                 dfs(board, word, i - 1, j, k + 1) ||
                 dfs(board, word, i, j + 1, k + 1) ||
                 dfs(board, word, i, j - 1, k + 1);
    board[i][j] = temp;
    return result;
}
