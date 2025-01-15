#include <vector>
#include <stack>

class Solution {
public:
    std::vector<int> dailyTemperatures(std::vector<int>& temperatures) {
        int n = temperatures.size();
        std::vector<int> result(n, 0);
        std::stack<int> stack;

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.empty() && temperatures[i] >= temperatures[stack.top()]) {
                stack.pop();
            }

            if (!stack.empty()) {
                result[i] = stack.top() - i;
            }

            stack.push(i);
        }

        return result;
    }
};
