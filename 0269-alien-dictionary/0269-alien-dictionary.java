
import java.util.*;

public class AlienDictionary {
    public String alienOrder(String[] words) {
        // Step 1: Create the graph.
        Map<Character, Set<Character>> adj = new HashMap<>();
        for (String word : words) {
            for (char c : word.toCharArray()) {
                adj.putIfAbsent(c, new HashSet<>());
            }
        }

        for (int i = 0; i < words.length - 1; i++) {
            String word1 = words[i];
            String word2 = words[i + 1];
            int minLen = Math.min(word1.length(), word2.length());

            // Handle the case where order is impossible.
            if (word1.length() > word2.length() && word1.substring(0, minLen).equals(word2.substring(0, minLen))) {
                return "";
            }

            for (int j = 0; j < minLen; j++) {
                if (word1.charAt(j) != word2.charAt(j)) {
                    adj.get(word1.charAt(j)).add(word2.charAt(j));
                    break;
                }
            }
        }

        // Step 2: Detect cycles and perform DFS.
        Map<Character, Boolean> visited = new HashMap<>();
        List<Character> order = new ArrayList<>();

        for (char c : adj.keySet()) {
            if (!visited.containsKey(c)) {
                if (!dfs(c, adj, visited, order)) {
                    return ""; // Cycle detected.
                }
            }
        }

        // Reverse the post-visit ordered list.
        Collections.reverse(order);
        StringBuilder result = new StringBuilder();
        for (char c : order) {
            result.append(c);
        }
        return result.toString();
    }

    private boolean dfs(char c, Map<Character, Set<Character>> adj, Map<Character, Boolean> visited, List<Character> order) {
        if (visited.containsKey(c)) {
            return visited.get(c); // If True, no cycle; if False, cycle detected.
        }
        visited.put(c, false);
        for (char nei : adj.get(c)) {
            if (!dfs(nei, adj, visited, order)) {
                return false; // Cycle detected.
            }
        }
        visited.put(c, true);
        order.add(c);
        return true;
    }
}
