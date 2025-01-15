#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
    // Step 1: Count the frequency of each element
    unordered_map<int, int> count;
    for (int num : nums) {
        count[num]++;
    }

    // Step 2: Use a priority queue (heap) to find the k most frequent elements
    auto comp = [&count](int a, int b) { return count[a] > count[b]; };
    priority_queue<int, vector<int>, decltype(comp)> heap(comp);
    for (auto& pair : count) {
        heap.push(pair.first);
        if (heap.size() > k) {
            heap.pop();
        }
    }

    // Step 3: Build output list from the heap
    vector<int> result;
    while (!heap.empty()) {
        result.push_back(heap.top());
        heap.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    vector<int> nums = {1, 1, 1, 2, 2, 3};
    int k = 2;
    vector<int> result = topKFrequent(nums, k);
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    return 0;
}
