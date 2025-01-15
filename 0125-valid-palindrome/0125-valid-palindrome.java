public class ValidPalindrome {
    public static boolean isPalindrome(String s) {
        // Step 1: Initialize two pointers
        int left = 0, right = s.length() - 1;

        // Step 2: Traverse the string from both ends
        while (left < right) {
            // Skip non-alphanumeric characters on the left
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            // Skip non-alphanumeric characters on the right
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            // Compare characters
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }

            // Move both pointers inward
            left++;
            right--;
        }

        return true;
    }

    public static void main(String[] args) {
        String s = "A man, a plan, a canal: Panama";
        System.out.println(isPalindrome(s));
    }
}
