
#include <iostream>
#include <vector>

using namespace std;

void rotate(vector<vector<int>>& matrix) {
    int n = matrix.size();

    // Iterate over each layer of the matrix
    for (int i = 0; i < n / 2; i++) {
        for (int j = i; j < n - i - 1; j++) {
            // Save the temp element
            int temp = matrix[i][j];

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

int main() {
    vector<vector<int>> matrix = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    rotate(matrix);

    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
