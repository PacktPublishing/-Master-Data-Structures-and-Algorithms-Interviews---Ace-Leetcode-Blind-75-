import java.util.Collections;
import java.util.PriorityQueue;

class MedianFinder {
    private PriorityQueue<Integer> leftHalf;
    private PriorityQueue<Integer> rightHalf;

    public MedianFinder() {
        leftHalf = new PriorityQueue<>(Collections.reverseOrder()); // Max-heap
        rightHalf = new PriorityQueue<>(); // Min-heap
    }

    public void addNum(int num) {
        if (leftHalf.isEmpty() || num <= leftHalf.peek()) {
            leftHalf.offer(num);
        } else {
            rightHalf.offer(num);
        }

        // Rebalance heaps
        if (leftHalf.size() > rightHalf.size() + 1) {
            rightHalf.offer(leftHalf.poll());
        } else if (rightHalf.size() > leftHalf.size()) {
            leftHalf.offer(rightHalf.poll());
        }
    }

    public double findMedian() {
        if (leftHalf.size() > rightHalf.size()) {
            return leftHalf.peek();
        } else if (rightHalf.size() > leftHalf.size()) {
            return rightHalf.peek();
        } else {
            return (leftHalf.peek() + rightHalf.peek()) / 2.0;
        }
    }
}

// Usage:
// MedianFinder obj = new MedianFinder();
// obj.addNum(num);
// double median = obj.findMedian();
