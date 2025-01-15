
class TrieNode {
    constructor() {
        this.children = {};
        this.isEnd = false;
    }
}

class WordDictionary {
    constructor() {
        this.root = new TrieNode();
    }

    addWord(word) {
        let node = this.root;
        for (let char of word) {
            if (!(char in node.children)) {
                node.children[char] = new TrieNode();
            }
            node = node.children[char];
        }
        node.isEnd = true;
    }

    search(word) {
        const dfs = (node, i) => {
            if (i === word.length) {
                return node.isEnd;
            }
            if (word[i] === '.') {
                for (let child in node.children) {
                    if (dfs(node.children[child], i + 1)) {
                        return true;
                    }
                }
                return false;
            } else {
                return word[i] in node.children && dfs(node.children[word[i]], i + 1);
            }
        };
        return dfs(this.root, 0);
    }
}
