
function isAnagram(s, t) {
    if (s.length !== t.length) {
        return false;
    }

    let count = {};

    for (let char of s) {
        count[char] = (count[char] || 0) + 1;
    }

    for (let char of t) {
        if (!count[char]) {
            return false;
        }
        count[char]--;
        if (count[char] < 0) {
            return false;
        }
    }

    return true;
}

console.log(isAnagram("anagram", "nagaram")); // true
console.log(isAnagram("rat", "car"));         // false
