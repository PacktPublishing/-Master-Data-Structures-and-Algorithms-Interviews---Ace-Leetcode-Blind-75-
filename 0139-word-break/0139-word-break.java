import java.util.*;

class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        boolean[] res = new boolean[s.length() + 1];
        res[0] = true;

        for (int i = 0; i <= s.length(); i++) {
            for (String word : wordSet) {
                if (res[i] && i + word.length() <= s.length() && s.substring(i, i + word.length()).equals(word)) {
                    res[i + word.length()] = true;
                }
            }
        }

        return res[s.length()];
    }
}
