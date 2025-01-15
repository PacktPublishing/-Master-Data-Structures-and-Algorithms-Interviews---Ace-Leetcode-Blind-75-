
#include <iostream>
#include <cstdint>

using namespace std;

uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0;

    for (int i = 0; i < 32; i++) {
        uint32_t bit = n & 1;  // Extract the last bit of n
        result = (result << 1) | bit;  // Shift result to the left and add bit
        n = n >> 1;  // Shift n to the right to process the next bit
    }

    return result;
}

int main() {
    uint32_t n = 43261596;  // Example input (binary: 00000010100101000001111010011100)
    cout << reverseBits(n) << endl;  // Output: 964176192 (binary: 00111001011110000010100101000000)

    return 0;
}
