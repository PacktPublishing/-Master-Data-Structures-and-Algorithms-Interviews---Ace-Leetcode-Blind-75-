
#include <iostream>
#include <unordered_map>
#include <string>

bool isAnagram(std::string s, std::string t) {
    if (s.length() != t.length()) {
        return false;
    }

    std::unordered_map<char, int> count;

    for (char c : s) {
        count[c]++;
    }

    for (char c : t) {
        if (count.find(c) == count.end()) {
            return false;
        }
        count[c]--;
        if (count[c] < 0) {
            return false;
        }
    }

    return true;
}

int main() {
    std::cout << std::boolalpha << isAnagram("anagram", "nagaram") << std::endl; // true
    std::cout << std::boolalpha << isAnagram("rat", "car") << std::endl;         // false
    return 0;
}
