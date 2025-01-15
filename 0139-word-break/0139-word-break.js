var wordBreak = function(s, wordDict) {
    const wordSet = new Set(wordDict);
    const res = Array(s.length + 1).fill(false);
    res[0] = true;

    for (let i = 0; i <= s.length; i++) {
        for (const word of wordSet) {
            if (res[i] && i + word.length <= s.length && s.substring(i, i + word.length) === word) {
                res[i + word.length] = true;
            }
        }
    }

    return res[s.length];
};
