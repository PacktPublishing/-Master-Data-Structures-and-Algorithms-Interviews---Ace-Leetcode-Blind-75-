# Contains Duplicate (Leetcode #217)

In this blog, we'll be tackling LeetCode problem 217: **"Contains Duplicate"**. It's a classic problem that tests your ability to effectively manage and analyze a dataset to check for the existence of duplicate elements. We'll go over the problem description, explore a brute force approach, provide hints for improving your solution, and ultimately explain an efficient way to solve it. Let's dive in!

### Understanding the Problem Statement

You are given an integer array `nums`. Your task is to determine if any value appears **at least twice** in the array. In other words, we need to return `true` if there are any duplicates, and `false` otherwise.

**Example**:

* Input: `nums = [1, 2, 3, 1]`
    
* Output: `true` (since `1` appears twice)
    
* Input: `nums = [1, 2, 3, 4]`
    
* Output: `false` (since no element appears more than once)
    

The challenge is to come up with a solution that runs efficiently for large input arrays.

### The Brute Force Approach

The most straightforward way to solve this problem is to compare every element with every other element in the array. This brute force approach works, but it has a significant drawback when it comes to efficiency.

Here's how a brute force solution would look:

```python
# Brute Force Solution
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

In this solution, we use two nested loops to compare each element to every other element, which gives us a time complexity of **O(n^2)**. While this approach will give the correct answer, it's not suitable for large datasets because it takes too long to process.

### Hint to Solve the Problem Efficiently

The brute force approach works but is very inefficient for large input arrays. The key to improving our solution is to leverage a data structure that allows us to perform checks in constant time. In particular, using a **set** in Python can be very helpful here, as sets do not allow duplicates and offer average **O(1)** lookup times.

Consider how a set can help us easily determine if an element has already been seen in the array.

### The Efficient Solution

Let's walk through the efficient solution to the problem using a **set**. This solution ensures we are only iterating through the list once, and our operations within the loop are performed in constant time on average.

Here's the code:

```python
# Efficient Solution
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Explanation**:

1. **Create a Set**: We start by creating an empty set named `seen` to keep track of numbers we've encountered.
    
2. **Iterate Through the List**: For each element in the list `nums`, we check if it is already in the set.
    
3. **Return True if Found**: If we find the element in the set, we know it is a duplicate, and we return `True`.
    
4. **Add the Number to Set**: If the element is not in the set, we add it to `seen`.
    
5. **Return False**: If we finish iterating through the list without finding any duplicates, we return `False`.
    

### Time and Space Complexity

* **Time Complexity**: The time complexity of the efficient solution is **O(n)**, where `n` is the number of elements in the array. We iterate through the list once, and the average time complexity for inserting and checking membership in a set is **O(1)**.
    
* **Space Complexity**: The space complexity is **O(n)** as well, because, in the worst case, we might need to store all `n` elements in the set if there are no duplicates.
    

### Summary

In this blog, we've covered LeetCode problem 217: "Contains Duplicate". We started with a brute force solution, which was straightforward but inefficient. By understanding the properties of a set, we improved our solution to achieve a time complexity of **O(n)** and a space complexity of **O(n)**, making it much more efficient for larger datasets.

If you're looking to enhance your problem-solving skills, always remember that finding the right data structure can make all the difference! Try implementing the efficient solution on your own, and you'll see how useful Python's set can be in situations like this.


Orignal Blog Source: [Contains Duplicate (Leetcode #217)](https://blog.unwiredlearning.com/contains-duplicate).