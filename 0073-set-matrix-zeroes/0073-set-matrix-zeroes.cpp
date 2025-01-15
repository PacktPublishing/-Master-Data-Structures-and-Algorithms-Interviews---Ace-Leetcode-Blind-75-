
#include <iostream>
#include <vector>

using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    int rows = matrix.size(), cols = matrix[0].size();
    bool firstRowZero = false, firstColZero = false;

    // Check if the first column needs to be zeroed
    for (int i = 0; i < rows; i++) {
        if (matrix[i][0] == 0) {
            firstColZero = true;
            break;
        }
    }

    // Check if the first row needs to be zeroed
    for (int j = 0; j < cols; j++) {
        if (matrix[0][j] == 0) {
            firstRowZero = true;
            break;
        }
    }

    // Use first row and column to mark zero rows and columns
    for (int i = 1; i < rows; i++) {
        for (int j = 1; j < cols; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // Zero out marked rows and columns
    for (int i = 1; i < rows; i++) {
        for (int j = 1; j < cols; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero out the first column if needed
    if (firstColZero) {
        for (int i = 0; i < rows; i++) {
            matrix[i][0] = 0;
        }
    }

    // Zero out the first row if needed
    if (firstRowZero) {
        for (int j = 0; j < cols; j++) {
            matrix[0][j] = 0;
        }
    }
}

int main() {
    vector<vector<int>> matrix = {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1}
    };
    setZeroes(matrix);

    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
