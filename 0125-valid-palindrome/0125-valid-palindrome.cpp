#include <iostream>
#include <cctype>
#include <string>

using namespace std;

bool isPalindrome(string s) {
    // Step 1: Initialize two pointers
    int left = 0, right = s.length() - 1;

    // Step 2: Traverse the string from both ends
    while (left < right) {
        // Skip non-alphanumeric characters on the left
        while (left < right && !isalnum(s[left])) {
            left++;
        }
        // Skip non-alphanumeric characters on the right
        while (left < right && !isalnum(s[right])) {
            right--;
        }

        // Compare characters
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }

        // Move both pointers inward
        left++;
        right--;
    }

    return true;
}

int main() {
    string s = "A man, a plan, a canal: Panama";
    cout << (isPalindrome(s) ? "true" : "false") << endl;
    return 0;
}
