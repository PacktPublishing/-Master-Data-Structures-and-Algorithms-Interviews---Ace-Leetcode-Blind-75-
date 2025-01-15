class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty stack to keep track of opening brackets
        stack = []

        # A mapping of closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "]": "[", "}": "{"}

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

        # After processing all characters, 
        # return True if the stack is empty (all brackets matched), else False
        return not stack


#Question: https://leetcode.com/problems/valid-parentheses
#Blog: https://blog.unwiredlearning.com/valid-parentheses