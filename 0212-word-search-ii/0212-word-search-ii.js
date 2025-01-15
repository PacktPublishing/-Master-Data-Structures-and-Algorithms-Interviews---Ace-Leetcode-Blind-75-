
class TrieNode {
    constructor() {
        this.children = {};
        this.isEnd = false;
    }
}

var findWords = function(board, words) {
    const root = buildTrie(words);
    const result = new Set();
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (root.children[board[i][j]]) {
                dfs(board, root, i, j, '', result);
            }
        }
    }
    return Array.from(result);
};

function buildTrie(words) {
    const root = new TrieNode();
    for (const word of words) {
        let node = root;
        for (const char of word) {
            if (!node.children[char]) {
                node.children[char] = new TrieNode();
            }
            node = node.children[char];
        }
        node.isEnd = true;
    }
    return root;
}

function dfs(board, node, i, j, path, result) {
    if (node.isEnd) {
        result.add(path);
        node.isEnd = false; // Avoid duplicates
    }
    if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || !node.children[board[i][j]]) {
        return;
    }
    const temp = board[i][j];
    board[i][j] = '#'; // Mark as visited
    for (const [x, y] of [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]) {
        dfs(board, node.children[temp], x, y, path + temp, result);
    }
    board[i][j] = temp; // Unmark
}
