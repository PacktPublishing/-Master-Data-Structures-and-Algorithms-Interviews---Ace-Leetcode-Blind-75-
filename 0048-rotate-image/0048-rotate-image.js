
function rotate(matrix) {
    let n = matrix.length;

    // Iterate over each layer of the matrix
    for (let i = 0; i < Math.floor(n / 2); i++) {
        for (let j = i; j < n - i - 1; j++) {
            // Save the temp element
            let temp = matrix[i][j];

            // Move bottom-left element to top-left
            matrix[i][j] = matrix[n - j - 1][i];

            // Move bottom-right element to bottom-left
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];

            // Move top-right element to bottom-right
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];

            // Assign temp element to top-right
            matrix[j][n - i - 1] = temp;
        }
    }
}

// Example usage:
let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

rotate(matrix);
console.log(matrix);
