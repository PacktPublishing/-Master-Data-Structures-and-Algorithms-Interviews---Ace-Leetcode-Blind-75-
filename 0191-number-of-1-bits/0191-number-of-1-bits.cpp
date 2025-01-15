
#include <iostream>

using namespace std;

int hammingWeight(uint32_t n) {
    int count = 0;

    // Assuming a 32-bit integer
    for (int i = 0; i < 32; i++) {
        count += (n & 1);
        n = n >> 1;
    }

    return count;
}

int main() {
    uint32_t n = 11;  // Example input (binary: 1011)
    cout << hammingWeight(n) << endl;  // Output: 3

    return 0;
}
