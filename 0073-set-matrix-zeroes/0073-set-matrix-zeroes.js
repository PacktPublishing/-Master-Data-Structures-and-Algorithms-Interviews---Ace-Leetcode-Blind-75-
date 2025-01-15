
function setZeroes(matrix) {
    let rows = matrix.length, cols = matrix[0].length;
    let firstRowZero = false, firstColZero = false;

    // Check if the first column needs to be zeroed
    for (let i = 0; i < rows; i++) {
        if (matrix[i][0] === 0) {
            firstColZero = true;
            break;
        }
    }

    // Check if the first row needs to be zeroed
    for (let j = 0; j < cols; j++) {
        if (matrix[0][j] === 0) {
            firstRowZero = true;
            break;
        }
    }

    // Use first row and column to mark zero rows and columns
    for (let i = 1; i < rows; i++) {
        for (let j = 1; j < cols; j++) {
            if (matrix[i][j] === 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // Zero out marked rows and columns
    for (let i = 1; i < rows; i++) {
        for (let j = 1; j < cols; j++) {
            if (matrix[i][0] === 0 || matrix[0][j] === 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero out the first column if needed
    if (firstColZero) {
        for (let i = 0; i < rows; i++) {
            matrix[i][0] = 0;
        }
    }

    // Zero out the first row if needed
    if (firstRowZero) {
        for (let j = 0; j < cols; j++) {
            matrix[0][j] = 0;
        }
    }
}

// Example usage:
let matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
];
setZeroes(matrix);
console.log(matrix);
