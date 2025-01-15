
function reverseBits(n) {
    let result = 0;

    for (let i = 0; i < 32; i++) {
        let bit = n & 1;  // Extract the last bit of n
        result = (result << 1) | bit;  // Shift result to the left and add bit
        n = n >>> 1;  // Logical right shift n to process the next bit
    }

    return result >>> 0;  // Convert to unsigned 32-bit integer
}

// Example usage:
let n = 43261596;  // Example input (binary: 00000010100101000001111010011100)
console.log(reverseBits(n));  // Output: 964176192 (binary: 00111001011110000010100101000000)
