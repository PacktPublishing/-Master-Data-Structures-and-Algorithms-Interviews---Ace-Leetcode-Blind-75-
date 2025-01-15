// JavaScript implementation of group anagrams
function groupAnagrams(strs) {
    let anagramMap = new Map();
    
    strs.forEach(word => {
        let count = new Array(26).fill(0);
        for (let i = 0; i < word.length; i++) {
            count[word.charCodeAt(i) - 'a'.charCodeAt(0)]++;
        }
        let key = count.join('#');
        if (!anagramMap.has(key)) {
            anagramMap.set(key, []);
        }
        anagramMap.get(key).push(word);
    });
    
    return Array.from(anagramMap.values());
}

const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(groupAnagrams(strs));
