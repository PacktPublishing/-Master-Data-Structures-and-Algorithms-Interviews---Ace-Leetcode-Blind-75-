function isPalindrome(s) {
    // Step 1: Initialize two pointers
    let left = 0, right = s.length - 1;

    // Step 2: Traverse the string from both ends
    while (left < right) {
        // Skip non-alphanumeric characters on the left
        while (left < right && !isAlphanumeric(s[left])) {
            left++;
        }
        // Skip non-alphanumeric characters on the right
        while (left < right && !isAlphanumeric(s[right])) {
            right--;
        }

        // Compare characters
        if (s[left].toLowerCase() !== s[right].toLowerCase()) {
            return false;
        }

        // Move both pointers inward
        left++;
        right--;
    }

    return true;
}

function isAlphanumeric(char) {
    return /^[a-zA-Z0-9]$/.test(char);
}

// Example usage
const s = "A man, a plan, a canal: Panama";
console.log(isPalindrome(s));
