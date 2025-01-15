function minWindow(s, t) {
    if (s.length === 0 || t.length === 0) return "";

    const dictT = {};
    for (let char of t) {
        dictT[char] = (dictT[char] || 0) + 1;
    }

    let required = Object.keys(dictT).length;
    let left = 0, right = 0, formed = 0;
    const windowCounts = {};
    let minLen = Infinity;
    let minLeft = 0, minRight = 0;

    while (right < s.length) {
        let char = s[right];
        windowCounts[char] = (windowCounts[char] || 0) + 1;

        if (dictT[char] && windowCounts[char] === dictT[char]) {
            formed++;
        }

        while (left <= right && formed === required) {
            char = s[left];

            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minLeft = left;
                minRight = right;
            }

            windowCounts[char]--;
            if (dictT[char] && windowCounts[char] < dictT[char]) {
                formed--;
            }

            left++;
        }

        right++;
    }

    return minLen === Infinity ? "" : s.substring(minLeft, minRight + 1);
}
