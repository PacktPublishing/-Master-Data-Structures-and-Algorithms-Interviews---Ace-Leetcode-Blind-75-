class MedianFinder {
  constructor() {
    this.leftHalf = new MaxHeap(); // Max-heap
    this.rightHalf = new MinHeap(); // Min-heap
  }

  addNum(num) {
    if (this.leftHalf.size() === 0 || num <= this.leftHalf.peek()) {
      this.leftHalf.add(num);
    } else {
      this.rightHalf.add(num);
    }

    // Rebalance heaps
    if (this.leftHalf.size() > this.rightHalf.size() + 1) {
      this.rightHalf.add(this.leftHalf.poll());
    } else if (this.rightHalf.size() > this.leftHalf.size()) {
      this.leftHalf.add(this.rightHalf.poll());
    }
  }

  findMedian() {
    if (this.leftHalf.size() > this.rightHalf.size()) {
      return this.leftHalf.peek();
    } else if (this.rightHalf.size() > this.leftHalf.size()) {
      return this.rightHalf.peek();
    } else {
      return (this.leftHalf.peek() + this.rightHalf.peek()) / 2;
    }
  }
}

// Heaps implementation:
class MaxHeap {
  constructor() {
    this.heap = [];
  }

  add(val) {
    this.heap.push(val);
    this.bubbleUp();
  }

  peek() {
    return this.heap[0];
  }

  poll() {
    if (this.heap.length > 1) {
      const max = this.heap[0];
      this.heap[0] = this.heap.pop();
      this.bubbleDown();
      return max;
    } else {
      return this.heap.pop();
    }
  }

  size() {
    return this.heap.length;
  }

  bubbleUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[index] <= this.heap[parentIndex]) break;
      [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
      index = parentIndex;
    }
  }

  bubbleDown() {
    let index = 0;
    const length = this.heap.length;
    while (true) {
      const leftChildIndex = 2 * index + 1;
      const rightChildIndex = 2 * index + 2;
      let largest = index;

      if (leftChildIndex < length && this.heap[leftChildIndex] > this.heap[largest]) {
        largest = leftChildIndex;
      }

      if (rightChildIndex < length && this.heap[rightChildIndex] > this.heap[largest]) {
        largest = rightChildIndex;
      }

      if (largest === index) break;
      [this.heap[index], this.heap[largest]] = [this.heap[largest], this.heap[index]];
      index = largest;
    }
  }
}

class MinHeap {
  constructor() {
    this.heap = [];
  }

  add(val) {
    this.heap.push(val);
    this.bubbleUp();
  }

  peek() {
    return this.heap[0];
  }

  poll() {
    if (this.heap.length > 1) {
      const min = this.heap[0];
      this.heap[0] = this.heap.pop();
      this.bubbleDown();
      return min;
    } else {
      return this.heap.pop();
    }
  }

  size() {
    return this.heap.length;
  }

  bubbleUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[index] >= this.heap[parentIndex]) break;
      [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
      index = parentIndex;
    }
  }

  bubbleDown() {
    let index = 0;
    const length = this.heap.length;
    while (true) {
      const leftChildIndex = 2 * index + 1;
      const rightChildIndex = 2 * index + 2;
      let smallest = index;

      if (leftChildIndex < length && this.heap[leftChildIndex] < this.heap[smallest]) {
        smallest = leftChildIndex;
      }

      if (rightChildIndex < length && this.heap[rightChildIndex] < this.heap[smallest]) {
        smallest = rightChildIndex;
      }

      if (smallest === index) break;
      [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
      index = smallest;
    }
  }
}