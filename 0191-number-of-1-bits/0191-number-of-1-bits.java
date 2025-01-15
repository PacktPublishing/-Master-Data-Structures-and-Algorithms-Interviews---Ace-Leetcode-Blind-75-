
public class NumberOf1Bits {
    public static int hammingWeight(int n) {
        int count = 0;

        // Assuming a 32-bit integer
        for (int i = 0; i < 32; i++) {
            count += (n & 1);
            n = n >> 1;
        }

        return count;
    }

    public static void main(String[] args) {
        int n = 11;  // Example input (binary: 1011)
        System.out.println(hammingWeight(n));  // Output: 3
    }
}
