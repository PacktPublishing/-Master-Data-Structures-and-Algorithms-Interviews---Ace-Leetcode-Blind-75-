# Valid Parentheses (Leetcode #20)

The 'Valid Parentheses' problem is a staple in coding interviews and serves as an excellent test of your understanding of stacks and data structures. It challenges your ability to correctly match different types of brackets, ensuring that they are properly nested and ordered. In this blog, we will explore a naive approach to solving this problem, provide a hint for an efficient solution, and then dive into an optimal approach using a stack. By the end, you'll have a thorough understanding of how to solve this problem efficiently.

## Understanding the Problem Statement

The 'Valid Parentheses' problem is a classic question often found in coding interviews. You are given a string that contains only the characters '(', ')', '\[', '\]', '{', and '}'. Your task is to determine if the input string is valid. A string is considered valid if the brackets are correctly closed in the correct order, meaning every opening bracket has a corresponding closing bracket, and they are nested properly.

For instance, the string "()\[\]{}" is valid because every type of bracket is closed correctly. However, "(\]" is not valid since the brackets are mismatched. Similarly, "(\[)\]" is not valid as the brackets are not properly nested.

## Brute Force Approach

One naive way to solve the problem is to iteratively search for matched pairs of parentheses and remove them from the string until there are no more pairs to remove. This method works by repeatedly replacing occurrences of "()", "\[\]", and "{}" with an empty string until none are left.

Although this approach will eventually determine if the string is valid, it is inefficient. The repeated scanning and string modification can lead to a time complexity of O(n^2) for a worst-case scenario, where 'n' is the length of the string. This approach also consumes extra space as it involves creating new strings during each iteration.

## Hint to Solve the Problem Efficiently

To solve this problem efficiently, think about using a data structure that allows you to easily track the order of opening brackets and quickly match them when closing brackets are found. Consider using a stack, which follows a Last In, First Out (LIFO) principle. Each time you encounter an opening bracket, push it onto the stack. When you encounter a closing bracket, check if it matches the most recently added opening bracket.

## Efficient Solution

Here is the efficient solution that makes use of a stack, as shown in the provided code:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []

        # A mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}

        # Iterate through each character in the string
        for character in s:
            if character in bracket_map:
                # If stack is not empty and the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == bracket_map[character]:
                    stack.pop()
                else:
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(character)

        # After processing all characters, return True if the stack is empty (all brackets matched), else False
        return not stack
```

**Explanation**:

* We use a stack to keep track of opening brackets.
    
* Whenever an opening bracket ('(', '\[', '{') is encountered, it is pushed onto the stack.
    
* When a closing bracket (')', '\]', '}') is encountered, we check if the stack is non-empty and if the top element of the stack matches the corresponding opening bracket. If it matches, we pop the element from the stack. If it doesn’t match or the stack is empty, we return `False`.
    
* At the end of the iteration, if the stack is empty, it means that all brackets have been matched properly, and we return `True`.
    

## Time and Space Complexity

* **Time Complexity**: O(n), where 'n' is the length of the input string. We traverse the string once, and each push and pop operation on the stack takes constant time, O(1).
    
* **Space Complexity**: O(n), where 'n' is the length of the input string. In the worst case, all characters in the string could be opening brackets, leading to a stack of size 'n'.
    

This solution is efficient and provides the correct result in a single pass through the string, making it significantly better than the brute force approach.

## Conclusion

The 'Valid Parentheses' problem is an excellent demonstration of how using the right data structure can make a significant difference in the efficiency of your solution. By leveraging a stack, we can solve this problem with linear time complexity, ensuring that every bracket is properly matched and nested. Whether you're preparing for coding interviews or just looking to improve your problem-solving skills, understanding this approach will serve you well in tackling similar problems involving balanced sequences.


README for [Valid Parentheses (Leetcode #20)](https://blog.unwiredlearning.com/valid-parentheses) was compiled from the Unwired Learning Blog.