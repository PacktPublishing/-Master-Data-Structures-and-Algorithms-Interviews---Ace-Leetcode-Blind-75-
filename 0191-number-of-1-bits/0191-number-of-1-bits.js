
function hammingWeight(n) {
    let count = 0;

    // Assuming a 32-bit integer
    for (let i = 0; i < 32; i++) {
        count += (n & 1);
        n = n >> 1;
    }

    return count;
}

// Example usage:
let n = 11;  // Example input (binary: 1011)
console.log(hammingWeight(n));  // Output: 3
