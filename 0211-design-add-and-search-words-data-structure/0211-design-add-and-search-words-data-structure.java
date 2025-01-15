
import java.util.HashMap;

class TrieNode {
    HashMap<Character, TrieNode> children;
    boolean isEnd;

    public TrieNode() {
        children = new HashMap<>();
        isEnd = false;
    }
}

class WordDictionary {

    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(word, root, 0);
    }

    private boolean dfs(String word, TrieNode node, int index) {
        if (index == word.length()) {
            return node.isEnd;
        }

        char c = word.charAt(index);
        if (c == '.') {
            for (TrieNode child : node.children.values()) {
                if (dfs(word, child, index + 1)) {
                    return true;
                }
            }
            return false;
        } else {
            return node.children.containsKey(c) && dfs(word, node.children.get(c), index + 1);
        }
    }
}
