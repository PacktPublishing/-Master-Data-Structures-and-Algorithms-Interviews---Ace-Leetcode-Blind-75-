
public class ReverseBits {
    public static int reverseBits(int n) {
        int result = 0;

        for (int i = 0; i < 32; i++) {
            int bit = n & 1;  // Extract the last bit of n
            result = (result << 1) | bit;  // Shift result to the left and add bit
            n = n >> 1;  // Shift n to the right to process the next bit
        }

        return result;
    }

    public static void main(String[] args) {
        int n = 43261596;  // Example input (binary: 00000010100101000001111010011100)
        System.out.println(reverseBits(n));  // Output: 964176192 (binary: 00111001011110000010100101000000)
    }
}
