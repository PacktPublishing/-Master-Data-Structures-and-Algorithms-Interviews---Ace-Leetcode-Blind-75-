def alienOrder(words):
    # Step 1: Create the graph.
    adj = {c: set() for word in words for c in word}
    
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        minLen = min(len(word1), len(word2))
        
        # Handle the case where order is impossible.
        if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
            return ""  
        
        for j in range(minLen):
            if word1[j] != word2[j]:
                adj[word1[j]].add(word2[j])
                break
    
    # Step 2: Detect cycles and perform DFS.
    visited = {}  # False = visited but not processed, True = processed.
    order = []
    
    def dfs(c):
        if c in visited:
            return visited[c]  # If True, no cycle; if False, cycle detected.
        visited[c] = False
        for nei in adj[c]:
            if dfs(nei) == False:
                return False  # Cycle detected.
        visited[c] = True
        order.append(c)
        return True
    
    for c in adj:
        if c not in visited:
            if not dfs(c):
                return ""  # Cycle detected.
    
    # Reverse the post-visit ordered list.
    return "".join(order[::-1])  


#Question: https://www.lintcode.com/problem/892/
#Blog: https://blog.unwiredlearning.com/alien-dictionary