function topKFrequent(nums, k) {
    // Step 1: Count the frequency of each element
    const count = new Map();
    for (const num of nums) {
        count.set(num, (count.get(num) || 0) + 1);
    }

    // Step 2: Use a priority queue (heap) to find the k most frequent elements
    const heap = new MinPriorityQueue({ priority: (a) => count.get(a) });
    for (const [key] of count) {
        heap.enqueue(key);
        if (heap.size() > k) {
            heap.dequeue();
        }
    }

    // Step 3: Build output list from the heap
    const result = [];
    while (heap.size() > 0) {
        result.push(heap.dequeue().element);
    }
    return result.reverse();
}

// Example usage
const nums = [1, 1, 1, 2, 2, 3];
const k = 2;
console.log(topKFrequent(nums, k));
