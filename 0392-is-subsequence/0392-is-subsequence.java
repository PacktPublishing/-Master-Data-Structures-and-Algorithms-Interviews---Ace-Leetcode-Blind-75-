
class Solution {
    public boolean isSubsequence(String str1, String str2) {
        int itr1 = 0, itr2 = 0;

        while (itr1 < str1.length() && itr2 < str2.length()) {
            if (str1.charAt(itr1) == str2.charAt(itr2)) {
                itr1++;
            }
            itr2++;
        }

        return itr1 == str1.length();
    }
}
