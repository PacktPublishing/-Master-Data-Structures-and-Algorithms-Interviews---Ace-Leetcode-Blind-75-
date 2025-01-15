#include <queue>
#include <vector>

class MedianFinder {
private:
    std::priority_queue<int> leftHalf; // Max-heap
    std::priority_queue<int, std::vector<int>, std::greater<int>> rightHalf; // Min-heap

public:
    MedianFinder() {
    }

    void addNum(int num) {
        if (leftHalf.empty() || num <= leftHalf.top()) {
            leftHalf.push(num);
        } else {
            rightHalf.push(num);
        }

        // Rebalance heaps
        if (leftHalf.size() > rightHalf.size() + 1) {
            rightHalf.push(leftHalf.top());
            leftHalf.pop();
        } else if (rightHalf.size() > leftHalf.size()) {
            leftHalf.push(rightHalf.top());
            rightHalf.pop();
        }
    }

    double findMedian() {
        if (leftHalf.size() > rightHalf.size()) {
            return leftHalf.top();
        } else if (rightHalf.size() > leftHalf.size()) {
            return rightHalf.top();
        } else {
            return (leftHalf.top() + rightHalf.top()) / 2.0;
        }
    }
};

// Usage:
// MedianFinder* obj = new MedianFinder();
// obj->addNum(num);
// double median = obj->findMedian();
