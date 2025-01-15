
#include <iostream>
#include <vector>

using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> result;
    if (matrix.empty()) return result;

    int rowBegin = 0, rowEnd = matrix.size() - 1;
    int colBegin = 0, colEnd = matrix[0].size() - 1;

    while (rowBegin <= rowEnd && colBegin <= colEnd) {
        for (int i = colBegin; i <= colEnd; i++) {
            result.push_back(matrix[rowBegin][i]);
        }
        rowBegin++;

        for (int i = rowBegin; i <= rowEnd; i++) {
            result.push_back(matrix[i][colEnd]);
        }
        colEnd--;

        if (rowBegin <= rowEnd) {
            for (int i = colEnd; i >= colBegin; i--) {
                result.push_back(matrix[rowEnd][i]);
            }
            rowEnd--;
        }

        if (colBegin <= colEnd) {
            for (int i = rowEnd; i >= rowBegin; i--) {
                result.push_back(matrix[i][colBegin]);
            }
            colBegin++;
        }
    }

    return result;
}

int main() {
    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    vector<int> result = spiralOrder(matrix);

    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
