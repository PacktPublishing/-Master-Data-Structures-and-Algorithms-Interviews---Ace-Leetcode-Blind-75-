
function countBits(n) {
    let result = new Array(n + 1).fill(0);

    if (n === 0) {
        return result;
    }

    result[1] = 1;

    for (let i = 2; i <= n; i++) {
        if (i % 2 === 0) {
            result[i] = result[Math.floor(i / 2)];
        } else {
            result[i] = result[Math.floor(i / 2)] + 1;
        }
    }

    return result;
}

// Example usage:
let n = 5;
console.log(countBits(n));
