
class Solution {
public:
    bool isSubsequence(string str1, string str2) {
        int itr1 = 0, itr2 = 0;

        while (itr1 < str1.length() && itr2 < str2.length()) {
            if (str1[itr1] == str2[itr2]) {
                itr1++;
            }
            itr2++;
        }

        return itr1 == str1.length();
    }
};
