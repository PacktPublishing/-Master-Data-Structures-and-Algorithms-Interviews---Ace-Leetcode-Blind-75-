
#include <iostream>
#include <vector>

using namespace std;

vector<int> countBits(int n) {
    vector<int> result(n + 1, 0);
    
    if (n == 0) {
        return result;
    }

    result[1] = 1;

    for (int i = 2; i <= n; i++) {
        if (i % 2 == 0) {
            result[i] = result[i / 2];
        } else {
            result[i] = result[i / 2] + 1;
        }
    }

    return result;
}

int main() {
    int n = 5;
    vector<int> result = countBits(n);

    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
