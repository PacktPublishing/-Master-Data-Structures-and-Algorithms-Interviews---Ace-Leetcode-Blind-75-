#include <algorithm>
#include <vector>

class Solution {
public:
    int numRescueBoats(std::vector<int>& people, int limit) {
        std::sort(people.begin(), people.end());
        int i = 0, j = people.size() - 1;
        int boats = 0;
        
        while (i <= j) {
            boats++;
            if (people[i] + people[j] <= limit) {
                i++;
            }
            j--;
        }
        
        return boats;
    }
};