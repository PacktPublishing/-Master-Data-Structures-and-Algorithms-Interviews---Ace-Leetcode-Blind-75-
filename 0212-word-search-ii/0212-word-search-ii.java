
import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

public class WordSearchII {
    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = buildTrie(words);
        Set<String> result = new HashSet<>();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (root.children.containsKey(board[i][j])) {
                    dfs(board, root, i, j, "", result);
                }
            }
        }
        return new ArrayList<>(result);
    }

    private TrieNode buildTrie(String[] words) {
        TrieNode root = new TrieNode();
        for (String word : words) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                node.children.putIfAbsent(c, new TrieNode());
                node = node.children.get(c);
            }
            node.isEnd = true;
        }
        return root;
    }

    private void dfs(char[][] board, TrieNode node, int i, int j, String path, Set<String> result) {
        if (node.isEnd) {
            result.add(path);
            node.isEnd = false; // Avoid duplicates
        }
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || !node.children.containsKey(board[i][j])) {
            return;
        }
        char temp = board[i][j];
        board[i][j] = '#'; // Mark as visited
        for (int[] dir : new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}) {
            int x = i + dir[0], y = j + dir[1];
            dfs(board, node.children.get(temp), x, y, path + temp, result);
        }
        board[i][j] = temp; // Unmark
    }
}
