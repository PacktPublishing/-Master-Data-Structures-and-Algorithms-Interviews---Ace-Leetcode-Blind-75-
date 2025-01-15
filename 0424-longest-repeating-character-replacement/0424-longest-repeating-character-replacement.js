function characterReplacement(s, k) {
    const count = {};
    let maxLen = 0;
    let left = 0;
    let maxFreq = 0;

    for (let right = 0; right < s.length; right++) {
        const char = s[right];
        count[char] = (count[char] || 0) + 1;
        maxFreq = Math.max(maxFreq, count[char]);

        while (right - left + 1 - maxFreq > k) {
            count[s[left]]--;
            left++;
        }

        maxLen = Math.max(maxLen, right - left + 1);
    }

    return maxLen;
}
