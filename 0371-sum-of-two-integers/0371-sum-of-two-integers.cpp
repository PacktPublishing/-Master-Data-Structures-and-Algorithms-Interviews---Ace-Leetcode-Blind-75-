
#include <iostream>

using namespace std;

int getSum(int a, int b) {
    // 32-bit integer max value
    int MAX = 0x7FFFFFFF;

    // Mask to get 32 bits
    unsigned int mask = 0xFFFFFFFF;

    while (b != 0) {
        // Calculate the carry bits
        unsigned int carry = (a & b) & mask;

        // XOR the bits for sum without carry
        a = (a ^ b) & mask;

        // Shift the carry to add in the next higher bit position
        b = (carry << 1) & mask;
    }

    // If a is negative, return a's complement in 32-bit format
    return a <= MAX ? a : ~(a ^ mask);
}

int main() {
    int a = 1, b = 2;
    cout << getSum(a, b) << endl;  // Output: 3

    return 0;
}
