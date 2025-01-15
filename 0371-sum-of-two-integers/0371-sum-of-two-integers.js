
function getSum(a, b) {
    // 32-bit integer max value
    const MAX = 0x7FFFFFFF;

    // Mask to get 32 bits
    const mask = 0xFFFFFFFF;

    while (b !== 0) {
        // Calculate the carry bits
        let carry = (a & b) & mask;

        // XOR the bits for sum without carry
        a = (a ^ b) & mask;

        // Shift the carry to add in the next higher bit position
        b = (carry << 1) & mask;
    }

    // If a is negative, return a's complement in 32-bit format
    return a <= MAX ? a : ~(a ^ mask);
}

// Example usage:
let a = 1, b = 2;
console.log(getSum(a, b));  // Output: 3
