
public class SumOfTwoIntegers {
    public static int getSum(int a, int b) {
        // 32-bit integer max value
        int MAX = 0x7FFFFFFF;
        
        // Mask to get 32 bits
        int mask = 0xFFFFFFFF;

        while (b != 0) {
            // Calculate the carry bits
            int carry = (a & b) & mask;

            // XOR the bits for sum without carry
            a = (a ^ b) & mask;

            // Shift the carry to add in the next higher bit position
            b = (carry << 1) & mask;
        }

        // If a is negative, return a's complement in 32-bit format
        return a <= MAX ? a : ~(a ^ mask);
    }

    public static void main(String[] args) {
        int a = 1, b = 2;
        System.out.println(getSum(a, b));  // Output: 3
    }
}
