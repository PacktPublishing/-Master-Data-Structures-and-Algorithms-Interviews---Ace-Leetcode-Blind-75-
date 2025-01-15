# Top K Frequent Elements (Leetcode #347)

In this blog, we will explore how to solve the Leetcode problem '347. Top K Frequent Elements.' We'll begin by understanding the problem, move through a common brute force approach, provide a hint to guide you towards the efficient solution, and finally explain the efficient solution in detail.

## Understanding the Problem Statement

The problem requires finding the **k most frequent elements** in a given list of integers. Given an integer array `nums` and an integer `k`, you need to return the `k` elements that appear most frequently. If there are multiple valid answers, any of them can be returned.

For example:

* **Input**: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2`
    
* **Output**: `[1, 2]`
    

The goal is to find the elements that occur most frequently in the given list and return exactly `k` such elements.

## Brute Force Approach

A common brute force approach to solving this problem would be:

1. **Count the Frequency**: Iterate through the list and count the frequency of each element. You could use a dictionary or a list to store the counts of each unique element.
    
2. **Sort by Frequency**: After counting, you would need to sort the unique elements by their frequency in descending order.
    
3. **Select Top K Elements**: Finally, select the top `k` elements from the sorted list.
    

This brute force method is simple but inefficient for large lists. Sorting the entire list based on frequency takes `O(n log n)` time, where `n` is the number of unique elements. In addition, counting the frequency takes `O(n)` time, making the entire approach fairly slow for large datasets.

## Hint to Solve the Problem Efficiently

To solve the problem more efficiently, consider using a **heap data structure**. The idea is to maintain the top `k` frequent elements without sorting the entire frequency list, which is where heaps come in handy.

The efficient solution consists of:

* Using a **dictionary** to count the frequencies of each element.
    
* Utilizing a **heap** to efficiently keep track of the `k` most frequent elements.
    

This approach helps reduce the time complexity significantly compared to the brute force approach.

## Efficient Solution

Let's dive into the efficient solution, following the code provided:

```python
from collections import Counter
import heapq

def topKFrequent(nums, k):
# Step 1: Count the frequency of each element
count = Counter(nums)  # O(n) time complexity

# Step 2: Use a heap to find the k most frequent elements
return heapq.nlargest(k, count.keys(), key=count.get)  # O(n log k) time complexity
```

**Step-by-Step Explanation**:

1. **Count Frequencies**: We use Python's `Counter` from the `collections` module to count the occurrences of each element in the list `nums`. This step takes `O(n)` time, where `n` is the number of elements in the list.
    
    ```python
    count = Counter(nums)  # count will be a dictionary-like object with frequencies
    ```
    
2. **Use a Heap**: After counting the frequencies, we use the `heapq.nlargest()` function to find the `k` most frequent elements. This function returns the `k` largest elements from the iterable based on a key function, which in this case is `count.get` to access the frequency of each element. Using a heap here allows us to maintain the top `k` elements efficiently without sorting the entire frequency list.
    
    ```python
    return heapq.nlargest(k, count.keys(), key=count.get)
    ```
    
    The use of `heapq.nlargest()` has a time complexity of `O(n log k)`, which is much more efficient than sorting the entire list.
    

## Time and Space Complexity

* **Time Complexity**: The time complexity of the solution is `O(n log k)`.
    
    * Counting the frequencies takes `O(n)` time.
        
    * Using the heap to extract the `k` most frequent elements takes `O(n log k)` time.
        
    * Therefore, the overall time complexity is dominated by `O(n log k)`.
        
* **Space Complexity**: The space complexity is `O(n)`. We require space for storing the frequency counts in a dictionary (`Counter`). The heap can take up to `k` space, but since `k <= n`, the space required is effectively `O(n)`.
    

## Conclusion

The efficient solution to finding the top `k` frequent elements leverages Python's `Counter` to count the occurrences of elements and `heapq.nlargest()` to retrieve the most frequent elements efficiently. This approach is particularly beneficial when dealing with larger datasets, as it reduces the need to sort the entire frequency dictionary.


README for [Top K Frequent Elements (Leetcode #347)](https://blog.unwiredlearning.com/top-k-frequent-elements) was compiled from the Unwired Learning Blog.