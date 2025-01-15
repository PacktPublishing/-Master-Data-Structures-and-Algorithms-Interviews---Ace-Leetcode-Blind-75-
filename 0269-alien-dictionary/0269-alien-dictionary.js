
function alienOrder(words) {
    // Step 1: Create the graph.
    const adj = {};
    for (const word of words) {
        for (const char of word) {
            if (!adj[char]) {
                adj[char] = new Set();
            }
        }
    }

    for (let i = 0; i < words.length - 1; i++) {
        const word1 = words[i];
        const word2 = words[i + 1];
        const minLen = Math.min(word1.length, word2.length);

        // Handle the case where order is impossible.
        if (word1.length > word2.length && word1.slice(0, minLen) === word2.slice(0, minLen)) {
            return "";
        }

        for (let j = 0; j < minLen; j++) {
            if (word1[j] !== word2[j]) {
                adj[word1[j]].add(word2[j]);
                break;
            }
        }
    }

    // Step 2: Detect cycles and perform DFS.
    const visited = {}; // false = visited but not processed, true = processed
    const order = [];

    function dfs(char) {
        if (visited.hasOwnProperty(char)) {
            return visited[char]; // If true, no cycle; if false, cycle detected.
        }
        visited[char] = false;
        for (const neighbor of adj[char]) {
            if (!dfs(neighbor)) {
                return false; // Cycle detected.
            }
        }
        visited[char] = true;
        order.push(char);
        return true;
    }

    for (const char in adj) {
        if (!visited.hasOwnProperty(char)) {
            if (!dfs(char)) {
                return ""; // Cycle detected.
            }
        }
    }

    // Reverse the post-visit ordered list.
    return order.reverse().join("");
}
