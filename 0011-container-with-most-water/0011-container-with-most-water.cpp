#include <iostream>
#include <vector>
#include <algorithm>

int maxArea(const std::vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;
    int maxArea = 0;

    while (left < right) {
        int area = std::min(height[left], height[right]) * (right - left);
        maxArea = std::max(maxArea, area);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea;
}

int main() {
    std::vector<int> height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    std::cout << "Maximum Area: " << maxArea(height) << std::endl;
    return 0;
}
